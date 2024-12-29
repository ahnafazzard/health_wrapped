import json
from datetime import datetime
from typing import Any, Dict, List

import pandas as pd

from zip_extract import HealthDataExtractor


class HealthDataParser:
    def __init__(self):
        self.workout_types = set()
        self.records = {
            "activity_summaries": [],
            "workouts": [],
            "heart_rate": [],
            "metadata": {},
        }

    def parse_date(self, date_str: str) -> datetime:
        """Parse date string to datetime object."""
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %z")

    def parse_metadata(self, export_date: Dict, me: Dict) -> None:
        """Parse metadata including export date and user information."""
        self.records["metadata"] = {
            "export_date": export_date.get("value"),
            "date_of_birth": me.get("HKCharacteristicTypeIdentifierDateOfBirth"),
            "biological_sex": me.get("HKCharacteristicTypeIdentifierBiologicalSex"),
            "blood_type": me.get("HKCharacteristicTypeIdentifierBloodType"),
            "skin_type": me.get("HKCharacteristicTypeIdentifierFitzpatrickSkinType"),
        }

    def parse_activity_summary(self, summary: Dict) -> None:
        """Parse activity summary data."""
        try:
            self.records["activity_summaries"].append(
                {
                    "date": summary.get("dateComponents"),
                    "active_calories": float(summary.get("activeEnergyBurned", 0)),
                    "active_calories_goal": float(
                        summary.get("activeEnergyBurnedGoal", 0)
                    ),
                    "exercise_minutes": int(summary.get("appleExerciseTime", 0)),
                    "exercise_goal": int(summary.get("appleExerciseTimeGoal", 0)),
                    "stand_hours": int(summary.get("appleStandHours", 0)),
                    "stand_goal": int(summary.get("appleStandHoursGoal", 0)),
                }
            )
        except (ValueError, TypeError) as e:
            print(f"Error parsing activity summary: {e}")

    def parse_workout(self, workout: Dict) -> None:
        """Parse workout data."""
        try:
            stats = workout.get("WorkoutStatistics", {})
            if stats:
                start_date = self.parse_date(stats.get("startDate", ""))
                end_date = self.parse_date(stats.get("endDate", ""))

                self.records["workouts"].append(
                    {
                        "date": start_date.strftime("%Y-%m-%d"),
                        "start_time": start_date.strftime("%H:%M:%S"),
                        "end_time": end_date.strftime("%H:%M:%S"),
                        "type": stats.get("type"),
                        "calories": float(stats.get("sum", 0)),
                        "unit": stats.get("unit"),
                        "average_mets": workout.get("MetadataEntry", {}).get(
                            "value", ""
                        ),
                    }
                )
        except (ValueError, TypeError) as e:
            print(f"Error parsing workout: {e}")

    def parse_record(self, record: Dict) -> None:
        """Parse health records including heart rate data."""
        try:
            hrv_data = record.get("HeartRateVariabilityMetadataList", {})
            if hrv_data and "InstantaneousBeatsPerMinute" in hrv_data:
                bpm_data = hrv_data["InstantaneousBeatsPerMinute"]
                self.records["heart_rate"].append(
                    {"bpm": int(bpm_data.get("bpm", 0)), "time": bpm_data.get("time")}
                )
        except (ValueError, TypeError) as e:
            print(f"Error parsing record: {e}")

    def parse_file(self, zip_path: str) -> Dict[str, Any]:
        """Main parsing function."""
        try:
            extractor = HealthDataExtractor(zip_path)
            health_data = extractor.get_data_dict()

            # Parse metadata
            self.parse_metadata(
                health_data.get("ExportDate", {}), health_data.get("Me", {})
            )

            # Parse records (including heart rate)
            if "Record" in health_data:
                self.parse_record(health_data["Record"])

            # Parse workouts
            if "Workout" in health_data:
                self.parse_workout(health_data["Workout"])

            # Parse activity summaries
            if "ActivitySummary" in health_data:
                self.parse_activity_summary(health_data["ActivitySummary"])

            # Convert to DataFrames
            dfs = {}
            for key, data in self.records.items():
                if data and isinstance(
                    data, list
                ):  # Only convert list data to DataFrame
                    dfs[key] = pd.DataFrame(data)
                    if "date" in dfs[key].columns:
                        dfs[key]["date"] = pd.to_datetime(dfs[key]["date"])

            # Calculate statistics
            stats = self.calculate_statistics(dfs)
            stats["metadata"] = self.records["metadata"]  # Include metadata in stats
            return stats

        except Exception as e:
            print(f"Error parsing health data: {e}")
            return {}

    def calculate_statistics(self, dfs: Dict[str, pd.DataFrame]) -> Dict[str, Any]:
        """Calculate statistics from the parsed data."""
        stats = {"activity_stats": {}, "workout_stats": {}, "heart_rate_stats": {}}

        # Activity statistics
        if "activity_summaries" in dfs:
            df = dfs["activity_summaries"]
            stats["activity_stats"] = {
                "avg_active_calories": round(df["active_calories"].mean(), 2),
                "total_active_calories": round(df["active_calories"].sum(), 2),
                "avg_exercise_minutes": round(df["exercise_minutes"].mean(), 2),
                "total_exercise_minutes": int(df["exercise_minutes"].sum()),
                "avg_stand_hours": round(df["stand_hours"].mean(), 2),
                "goal_completion_rate": {
                    "calories": round(
                        (df["active_calories"] >= df["active_calories_goal"]).mean()
                        * 100,
                        2,
                    ),
                    "exercise": round(
                        (df["exercise_minutes"] >= df["exercise_goal"]).mean() * 100, 2
                    ),
                    "stand": round(
                        (df["stand_hours"] >= df["stand_goal"]).mean() * 100, 2
                    ),
                },
            }

        # Workout statistics
        if "workouts" in dfs:
            df = dfs["workouts"]
            stats["workout_stats"] = {
                "total_workouts": len(df),
                "total_calories": round(df["calories"].sum(), 2),
                "avg_calories_per_workout": round(df["calories"].mean(), 2),
            }

        # Heart rate statistics
        if "heart_rate" in dfs:
            df = dfs["heart_rate"]
            stats["heart_rate_stats"] = {
                "avg_bpm": round(df["bpm"].mean(), 2),
                "max_bpm": int(df["bpm"].max()),
                "min_bpm": int(df["bpm"].min()),
            }

        return stats


def parse_health_data(zip_path: str) -> Dict[str, Any]:
    """Main function to parse health data."""
    parser = HealthDataParser()
    return parser.parse_file(zip_path)


if __name__ == "__main__":
    zip_file_path = "export.zip"
    stats = parse_health_data(zip_file_path)
    print(json.dumps(stats, indent=2))
