import json
from pathlib import Path
from typing import Dict, List, Set


def load_health_data(file_path: str) -> Dict:
    """Load Apple Health data from JSON file."""
    with open(file_path) as f:
        return json.load(f)


def get_record_types(data: Dict) -> Set[str]:
    """Extract all unique record types from health data."""
    return {record["type"] for record in data["Record"]}


def get_sample_workouts(data: Dict, samples_per_type: int = 5) -> Dict:
    """Get sample workouts for each workout type."""
    samples = {}
    for record in data["Workout"]:
        workout_type = record["workoutActivityType"]
        if workout_type not in samples:
            samples[workout_type] = []
        if len(samples[workout_type]) < samples_per_type:
            samples[workout_type].append(record)
    return samples


def validate_workout_data(workouts: Dict) -> tuple[bool, list[str]]:
    """Validate workout data structure and required fields.

    Returns:
        tuple: (is_valid, list of error messages)
    """
    errors = []

    if not workouts:
        return True, []

    for workout_type, workout_list in workouts.items():
        try:
            for workout in workout_list:
                if not isinstance(workout, dict):
                    errors.append(f"Invalid workout format for {workout_type}")
                    continue

                if "WorkoutStatistics" not in workout:
                    errors.append(
                        f"Missing WorkoutStatistics in {workout_type} workout"
                    )
                    continue

                if not isinstance(workout["WorkoutStatistics"], list):
                    errors.append(
                        f"Invalid WorkoutStatistics format in {workout_type} workout"
                    )
                    continue

                if not any(
                    isinstance(stat, dict)
                    and stat.get("type") == "HKQuantityTypeIdentifierActiveEnergyBurned"
                    for stat in workout["WorkoutStatistics"]
                ):
                    errors.append(
                        f"Missing ActiveEnergyBurned stat in {workout_type} workout"
                    )

        except Exception as e:
            errors.append(f"Error processing {workout_type}: {str(e)}")

    return len(errors) == 0, errors


def extract_record_samples(
    data: Dict, record_type: str, sample_size: int = 100
) -> List:
    """Extract sample records of a specific type."""
    records = filter(lambda x: x["type"] == record_type, data.get("Record", []))
    return list(records)[:sample_size]


def save_records(records: List, filename: str):
    """Save records to JSON file."""
    with open(filename, "w") as f:
        json.dump(records, f, indent=2)


def main():
    # File paths
    data_dir = Path("sample_data")
    input_file = data_dir / "export.json"

    # Load data
    data = load_health_data(input_file)
    print("Available data keys:", data.keys())

    # Get and display record types
    record_types = get_record_types(data)
    print("\nFound record types:", record_types)

    # Get and validate sample workouts
    sample_workouts = get_sample_workouts(data)
    validate_workout_data(sample_workouts)

    # Extract samples of different record types
    record_types_to_extract = {
        "HKQuantityTypeIdentifierDistanceWalkingRunning": "distance_walking_running",
        "HKQuantityTypeIdentifierStepCount": "step_count",
        "HKQuantityTypeIdentifierVO2Max": "vo2_max",
        "HKQuantityTypeIdentifierActiveEnergyBurned": "active_energy",
    }

    # Extract and save samples
    for record_type, filename in record_types_to_extract.items():
        records = extract_record_samples(data, record_type)
        save_records(records, data_dir / f"{filename}_samples.json")


if __name__ == "__main__":
    main()
