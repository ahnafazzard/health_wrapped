# main.py
import io
import json
import tempfile
import zipfile
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List

import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from health_records import HealthRecords
from schemas import HealthResponse
from workout_records import WorkoutRecords
from zip_extract import HealthDataExtractor

app = FastAPI()

# Add CORS middleware with more explicit settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only. In production, use specific origins
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,  # Set to False since we're using allow_origins=["*"]
    expose_headers=["*"],
    max_age=3600,
)


def _make_json_serializable(obj: Any) -> Any:
    """
    Recursively converts datetime objects to strings in nested data structures.
    Works with dictionaries, lists, and primitive types.
    """
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d")
    elif isinstance(obj, dict):
        return {k: _make_json_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [_make_json_serializable(item) for item in obj]
    elif isinstance(obj, (int, float, str, bool)) or obj is None:
        return obj
    else:
        return str(obj)  # Fallback for unknown types


@app.get("/test")
async def test():
    return JSONResponse(
        content={"message": "API is working"},
        headers={"Access-Control-Allow-Origin": "*"},
    )


@app.post("/upload")
async def upload_file(file: UploadFile):
    try:
        # Read the uploaded file into memory
        contents = await file.read()

        # Create a ZipFile object from the contents
        with zipfile.ZipFile(io.BytesIO(contents)) as zip_file:
            # Get list of files in the ZIP
            files = zip_file.namelist()

            # Get file sizes and info
            file_info = {}
            total_size = 0

            for filename in files:
                info = zip_file.getinfo(filename)
                file_info[filename] = {
                    "compressed_size": info.compress_size,
                    "uncompressed_size": info.file_size,
                    "compression_ratio": (
                        round((1 - info.compress_size / info.file_size) * 100, 2)
                        if info.file_size > 0
                        else 0
                    ),
                }
                total_size += info.file_size

            return JSONResponse(
                content={
                    "filename": file.filename,
                    "content_type": file.content_type,
                    "total_files": len(files),
                    "total_size_bytes": total_size,
                    "files": files,
                    "detailed_info": file_info,
                },
                headers={"Access-Control-Allow-Origin": "*"},
            )

    except zipfile.BadZipFile:
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid ZIP file"},
            headers={"Access-Control-Allow-Origin": "*"},
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)},
            headers={"Access-Control-Allow-Origin": "*"},
        )


@app.post("/api/upload_health_data", response_model=HealthResponse)
async def upload_health_data(file: UploadFile = File(...)):
    """Handle the upload of Apple Health data zip file"""
    try:
        print("Starting upload_health_data function")  # Debug log

        if not file.filename.endswith(".zip"):
            raise HTTPException(400, detail="File must be a zip file")

        print("Creating temporary file")  # Debug log
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_path = temp_file.name
            print(f"Temporary file created at: {temp_path}")  # Debug log

        try:
            print("Initializing HealthDataExtractor")  # Debug log
            # Use your HealthDataExtractor
            extractor = HealthDataExtractor(temp_path)
            print("Getting data dict")  # Debug log
            health_data = extractor.get_data_dict()
            print("Got health data:", type(health_data))  # Debug log

            print("Initializing HealthRecords")  # Debug log
            # Initialize records
            health_records = HealthRecords(health_data)
            print("Initializing WorkoutRecords")  # Debug log
            workout_records = WorkoutRecords(health_data)

            # Get current year metrics
            year = 2024  # You might want to make this configurable

            print("Building metrics dictionary")  # Debug log
            metrics = {
                "health": {
                    "total_steps": health_records.get_total_steps_for_year(year),
                    "total_distance": health_records.get_total_distance_for_year(year),
                    "total_calories": health_records.get_total_calories_for_year(year),
                    "average_vo2max": health_records.get_average_vo2max(year),
                    "weekly_stats": health_records.get_stats_by_week(year),
                    "best_week": health_records.get_best_week(year),
                },
                "workouts": {
                    "stats_by_type": workout_records.get_workout_stats_by_type(year),
                    "total_calories": workout_records.get_total_active_calories_for_year(
                        year
                    ),
                },
            }

            print("Making metrics JSON serializable")  # Debug log
            # Make the metrics JSON serializable
            metrics = _make_json_serializable(metrics)
            print("Returning metrics")  # Debug log

            return JSONResponse(
                content=metrics, headers={"Access-Control-Allow-Origin": "*"}
            )

        except Exception as e:
            print(f"Error processing health data: {str(e)}")  # Debug log
            print(f"Error type: {type(e)}")  # Debug log
            import traceback

            print(f"Traceback: {traceback.format_exc()}")  # Debug log
            raise HTTPException(500, detail=f"Error processing health data: {str(e)}")

    except Exception as e:
        print(f"Outer error: {str(e)}")  # Debug log
        print(f"Outer error type: {type(e)}")  # Debug log
        import traceback

        print(f"Outer traceback: {traceback.format_exc()}")  # Debug log
        raise HTTPException(500, detail=str(e))
    finally:
        # Clean up temp file
        try:
            Path(temp_path).unlink()
            print("Temporary file cleaned up")  # Debug log
        except Exception as e:
            print(f"Error cleaning up temp file: {str(e)}")  # Debug log


if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=8000, log_level="debug"  # Added debug logging
    )
