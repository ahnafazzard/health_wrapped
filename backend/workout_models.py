# workout_models.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Workout:
    activity_type: str
    creation_date: datetime
    start_date: datetime
    end_date: datetime
    workout_duration: float
    workout_duration_unit: str
    active_energy: Optional[float] = None
    active_energy_unit: Optional[str] = None
    heart_rate_avg: Optional[float] = None
    heart_rate_min: Optional[float] = None
    heart_rate_max: Optional[float] = None
    heart_rate_unit: Optional[str] = None

    def __init__(self, record: dict):
        self.activity_type = record["workoutActivityType"][
            len("HKWorkoutActivityType") :
        ]
        self.creation_date = datetime.strptime(
            record["creationDate"], "%Y-%m-%d %H:%M:%S %z"
        )
        self.start_date = datetime.strptime(record["startDate"], "%Y-%m-%d %H:%M:%S %z")
        self.end_date = datetime.strptime(record["endDate"], "%Y-%m-%d %H:%M:%S %z")
        self.workout_duration = float(record["duration"])
        self.workout_duration_unit = record["durationUnit"]

        # Process WorkoutStatistics
        if "WorkoutStatistics" in record:
            stats = record["WorkoutStatistics"]
            if isinstance(stats, dict):
                stats = [stats]

            for stat in stats:
                if stat["type"] == "HKQuantityTypeIdentifierActiveEnergyBurned":
                    self.active_energy = float(stat["sum"])
                    self.active_energy_unit = stat["unit"]
                elif stat["type"] == "HKQuantityTypeIdentifierHeartRate":
                    self.heart_rate_avg = float(stat["average"])
                    self.heart_rate_min = float(stat["minimum"])
                    self.heart_rate_max = float(stat["maximum"])
                    self.heart_rate_unit = stat["unit"]
