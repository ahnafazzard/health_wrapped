# workout_records.py
from datetime import datetime, timedelta
from itertools import groupby
from operator import itemgetter
from typing import Any, Dict, List, Optional, Tuple

from workout_models import Workout


class WorkoutRecords:
    def __init__(self, workout_data: Dict[str, List[Dict]]):
        self.records = workout_data.get("Workout", [])
        self.workouts = []
        # Process each workout
        for workout in self.records:
            self.workouts.append(Workout(workout))

    def _filter_workouts_by_year(
        self, year: int = datetime.now().year
    ) -> List[Workout]:
        return [workout for workout in self.workouts if workout.start_date.year == year]

    def get_total_active_calories_for_year(
        self, year: int = datetime.now().year
    ) -> Tuple[float, str]:
        yearly_workouts = self._filter_workouts_by_year(year)
        workouts_with_calories = [
            w for w in yearly_workouts if w.active_energy is not None
        ]
        if not workouts_with_calories:
            return 0.0, "Cal"
        unit = workouts_with_calories[0].active_energy_unit
        return round(sum(w.active_energy for w in workouts_with_calories), 2), unit

    def get_workout_stats_by_type(
        self, year: int = datetime.now().year
    ) -> Dict[str, Dict]:
        yearly_workouts = self._filter_workouts_by_year(year)

        stats = {}
        for activity_type, workouts in groupby(
            sorted(yearly_workouts, key=lambda x: x.activity_type),
            key=lambda x: x.activity_type,
        ):
            workouts = list(workouts)
            workouts_with_hr = [w for w in workouts if w.heart_rate_avg is not None]

            stats[activity_type] = {
                "count": len(workouts),
                "total_duration": round(sum(w.workout_duration for w in workouts), 2),
                "total_calories": round(sum(w.active_energy or 0 for w in workouts), 2),
                "avg_heart_rate": (
                    round(
                        sum(w.heart_rate_avg for w in workouts_with_hr)
                        / len(workouts_with_hr),
                        2,
                    )
                    if workouts_with_hr
                    else None
                ),
            }

        return stats

    def get_workouts_by_month(
        self, year: int = datetime.now().year
    ) -> Dict[int, List[Workout]]:
        yearly_workouts = self._filter_workouts_by_year(year)
        return {
            month: list(workouts)
            for month, workouts in groupby(
                sorted(yearly_workouts, key=lambda x: x.start_date.month),
                key=lambda x: x.start_date.month,
            )
        }

    def get_highest_calorie_activity(self, year: int = datetime.now().year) -> Dict:
        """Returns the activity type with highest average calories burned per workout"""
        yearly_workouts = self._filter_workouts_by_year(year)

        activity_calories = {}
        for activity_type, workouts in groupby(
            sorted(yearly_workouts, key=lambda x: x.activity_type),
            key=lambda x: x.activity_type,
        ):
            workouts = list(workouts)
            workouts_with_calories = [
                w for w in workouts if w.active_energy is not None
            ]
            if workouts_with_calories:
                avg_calories = sum(
                    w.active_energy for w in workouts_with_calories
                ) / len(workouts_with_calories)
                activity_calories[activity_type] = {
                    "average_calories": round(avg_calories, 2),
                    "total_calories": round(
                        sum(w.active_energy for w in workouts_with_calories), 2
                    ),
                    "workout_count": len(workouts_with_calories),
                }

        if not activity_calories:
            return {}

        highest_activity = max(
            activity_calories.items(), key=lambda x: x[1]["average_calories"]
        )
        return {highest_activity[0]: highest_activity[1]}

    def get_most_frequent_workout(self, year: int = datetime.now().year) -> Dict:
        """Returns the most common workout type"""
        yearly_workouts = self._filter_workouts_by_year(year)

        workout_counts = {}
        for activity_type, workouts in groupby(
            sorted(yearly_workouts, key=lambda x: x.activity_type),
            key=lambda x: x.activity_type,
        ):
            workout_counts[activity_type] = len(list(workouts))

        if not workout_counts:
            return {}

        most_frequent = max(workout_counts.items(), key=itemgetter(1))
        return {most_frequent[0]: most_frequent[1]}

    def get_peak_calorie_weeks(self, year: int = datetime.now().year) -> List[Dict]:
        """Returns weekly calorie totals, sorted by calories burned"""
        yearly_workouts = self._filter_workouts_by_year(year)

        # Group workouts by week
        week_groups = {}
        for workout in yearly_workouts:
            if workout.active_energy is None:
                continue
            week_num = workout.start_date.isocalendar()[1]
            if week_num not in week_groups:
                week_groups[week_num] = {
                    "week": week_num,
                    "total_calories": 0,
                    "workout_count": 0,
                    "start_date": None,
                    "end_date": None,
                }
            week_groups[week_num]["total_calories"] += workout.active_energy
            week_groups[week_num]["workout_count"] += 1

            # Update date range
            if (
                week_groups[week_num]["start_date"] is None
                or workout.start_date < week_groups[week_num]["start_date"]
            ):
                week_groups[week_num]["start_date"] = workout.start_date
            if (
                week_groups[week_num]["end_date"] is None
                or workout.end_date > week_groups[week_num]["end_date"]
            ):
                week_groups[week_num]["end_date"] = workout.end_date

        # Sort weeks by calories
        return sorted(
            week_groups.values(), key=lambda x: x["total_calories"], reverse=True
        )

    def get_missed_workout_days(
        self, year: int = datetime.now().year
    ) -> List[datetime]:
        """Returns dates with no workouts"""
        yearly_workouts = self._filter_workouts_by_year(year)

        # Get all workout dates
        workout_dates = {workout.start_date.date() for workout in yearly_workouts}

        # Generate all dates for the year
        year_start = datetime(year, 1, 1).date()
        year_end = datetime(year, 12, 31).date()
        all_dates = {
            year_start + timedelta(days=x)
            for x in range((year_end - year_start).days + 1)
        }

        # Return missed dates
        return sorted(list(all_dates - workout_dates))

    def get_average_heart_rate(
        self, year: int = datetime.now().year
    ) -> Dict[str, float]:
        """Returns average heart rate by activity type"""
        yearly_workouts = self._filter_workouts_by_year(year)

        hr_by_activity = {}
        for activity_type, workouts in groupby(
            sorted(yearly_workouts, key=lambda x: x.activity_type),
            key=lambda x: x.activity_type,
        ):
            workouts = list(workouts)
            workouts_with_hr = [w for w in workouts if w.heart_rate_avg is not None]
            if workouts_with_hr:
                hr_by_activity[activity_type] = {
                    "average": round(
                        sum(w.heart_rate_avg for w in workouts_with_hr)
                        / len(workouts_with_hr),
                        2,
                    ),
                    "highest": max(w.heart_rate_max for w in workouts_with_hr),
                    "lowest": min(w.heart_rate_min for w in workouts_with_hr),
                    "workout_count": len(workouts_with_hr),
                }

        return hr_by_activity


if __name__ == "__main__":
    import json

    with open("sample_data/export.json", "r") as f:
        data = json.load(f)

    records = WorkoutRecords(data)

    year = 2024

    peak_calorie_weeks = records.get_peak_calorie_weeks(year)
    peak_calorie_weeks = list(
        map(
            lambda x: {
                k: v.strftime("%Y-%m-%d") if isinstance(v, datetime) else v
                for k, v in x.items()
            },
            peak_calorie_weeks,
        )
    )

    results = {
        f"total_workout_calories_{year}": " ".join(
            map(str, records.get_total_active_calories_for_year(year))
        ),
        f"workout_stats_by_type_{year}": records.get_workout_stats_by_type(year),
        f"highest_calorie_activity_{year}": records.get_highest_calorie_activity(year),
        f"most_frequent_workout_{year}": records.get_most_frequent_workout(year),
        f"peak_calorie_weeks_{year}": peak_calorie_weeks,
        f"missed_workout_days_{year}": list(
            map(lambda x: x.strftime("%Y-%m-%d"), records.get_missed_workout_days(year))
        ),
        f"average_heart_rate_{year}": records.get_average_heart_rate(year),
    }

    # Also show monthly breakdown
    monthly_workouts = records.get_workouts_by_month(year)
    results["monthly_workouts"] = {}
    for month, workouts in monthly_workouts.items():
        results["monthly_workouts"][f"month_{month}"] = {
            "count": len(workouts),
            "calories": round(sum(w.active_energy or 0 for w in workouts), 2),
        }

    output = json.dumps(results, indent=2)
    print(output)

    with open("logfiles/test_workout_records_log.json", "w") as f:
        f.write(output)
