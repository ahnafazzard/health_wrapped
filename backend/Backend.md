# Backend

The backend system processes and analyzes Apple Health data exported from iOS devices. It provides REST API endpoints for uploading health data and retrieving analyzed metrics.

## Project Structure

```
health_wrapped/
├── .gitignore
├── README.md
├── environment.yml
├── setup.sh
├── backend/
│   ├── zip_extract.py (1)
│   ├── health_models.py (2)
│   ├── health_records.py (2)
│   ├── workout_models.py (3)
│   ├── workout_records.py (3)
│   ├── schemas.py (4)
│   ├── main.py (4)
│   ├── test_upload.html (4)
│   ├── Backend.md
├── sample_data/
│   ├── explore_data.py
│   ├── export.zip
│   ├── <generated sample data files ...>
├── ...
```

## Components

### 1. Data Extraction (`zip_extract.py`)

Handles the initial processing of Apple Health data:
- Takes raw `export.zip` file from user uploads
- Extracts and parses XML data into JSON format
- Creates processed `export.json` containing relevant health and workout data

Usage:
```python
extractor = HealthDataExtractor("path/to/export.zip")
health_data = extractor.get_data_dict()
```

### 2. Health Metrics Processing

#### Models (`health_models.py`)
Defines data models for health records:
- BaseHealthRecord
- DistanceWalkingRunningRecord
- StepCountRecord
- VO2MaxRecord
- ActiveEnergyBurnedRecord

#### Analytics (`health_records.py`)
Provides health metric calculations including:
- Total steps per year
- Total distance walked/run
- Total calories burned
- Average VO2 max
- Weekly statistics
- Best performing weeks

### 3. Workout Metrics Processing

#### Models (`workout_models.py`)
Defines the Workout data model containing:
- Activity type
- Duration
- Energy burned
- Heart rate statistics

#### Analytics (`workout_records.py`)
Provides workout analysis including:
- Total workout calories
- Statistics by workout type
- Highest calorie activities
- Most frequent workouts
- Peak calorie weeks
- Missed workout days
- Heart rate analysis by activity

### 4. API Layer

#### Data Models (`schemas.py`)
Defines Pydantic models for API responses:
- WeeklyStats
- HealthMetrics
- WorkoutMetrics
- HealthResponse

#### API Endpoints (`main.py`)

1. Test Connection
```
GET /test
Response: {"message": "API is working"}
```

2. Upload Health Data
```
POST /upload
Accepts: ZIP file
Response: File analysis and validation
```

3. Process Health Data
```
POST /api/upload_health_data
Accepts: ZIP file
Response: Processed health and workout metrics
```

#### Sample Response Format

```json
{
  "health": {
    "total_steps": [3363195, "step(s)"],
    "total_distance": [2595.92, "km"],
    "total_calories": [136783.57, "Cal"],
    "average_vo2max": [38.79, "mL/min·kg"],
    "weekly_stats": [...],
    "best_week": {...}
  },
  "workouts": {
    "stats_by_type": {...},
    "total_calories": [70137.59, "Cal"]
  }
}
```

## Development

1. Place sample `export.zip` in `backend/sample_data/`
2. Run `zip_extract.py` to generate processed JSON
3. Use `test_upload.html` for local API testing

## Error Handling

The backend includes comprehensive error handling for:
- Invalid ZIP files
- Malformed health data
- Processing errors
- API request validation

## CORS Configuration

The API includes CORS middleware configured for development with:
- All origins allowed (*)
- All methods allowed
- 1-hour max age
- Exposed headers

Note: Production deployment should restrict CORS settings to specific origins.