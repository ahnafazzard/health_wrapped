# boutta cook

import xml.etree.ElementTree as ET
import zipfile
import pandas as pd
import json
from datetime import datetime
from typing import Dict, List, Any
import tempfile
import os

class HealthDataParser:
    def __init__(self):
        self.workout_types = set()
        self.records = {
            'steps': [],
            'distance': [],
            'active_energy': [],
            'workouts': [],
            'heart_rate': []
        }

    def extract_zip(self, zip_path: str) -> str:
        """Extract the export.xml file from the zip archive."""
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
                # Apple Health data is typically in apple_health_export/export.xml
                xml_path = os.path.join(temp_dir, 'apple_health_export', 'export.xml')
                return xml_path

    def parse_date(self, date_str: str) -> datetime:
        """Parse date string to datetime object."""
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S %z')

    def is_current_year(self, date: datetime) -> bool:
        """Check if the date is from the current year."""
        current_year = datetime.now().year
        return date.year == current_year

    def parse_record(self, record: ET.Element) -> None:
        """Parse individual record elements."""
        try:
            start_date = self.parse_date(record.get('startDate', ''))
            
            if not self.is_current_year(start_date):
                return

            type_ = record.get('type')
            value = float(record.get('value', 0))
            
            record_data = {
                'date': start_date.strftime('%Y-%m-%d'),
                'timestamp': start_date.strftime('%Y-%m-%d %H:%M:%S'),
                'value': value
            }

            if type_ == 'HKQuantityTypeIdentifierStepCount':
                self.records['steps'].append(record_data)
            elif type_ == 'HKQuantityTypeIdentifierDistanceWalkingRunning':
                self.records['distance'].append(record_data)
            elif type_ == 'HKQuantityTypeIdentifierActiveEnergyBurned':
                self.records['active_energy'].append(record_data)
            elif type_ == 'HKQuantityTypeIdentifierHeartRate':
                self.records['heart_rate'].append(record_data)

        except (ValueError, TypeError) as e:
            print(f"Error parsing record: {e}")

    def parse_workout(self, workout: ET.Element) -> None:
        """Parse workout elements."""
        try:
            start_date = self.parse_date(workout.get('startDate', ''))
            
            if not self.is_current_year(start_date):
                return

            workout_type = workout.get('workoutActivityType', '')
            duration = float(workout.get('duration', 0))
            calories = float(workout.get('totalEnergyBurned', 0))
            distance = float(workout.get('totalDistance', 0))

            self.workout_types.add(workout_type)
            
            self.records['workouts'].append({
                'date': start_date.strftime('%Y-%m-%d'),
                'timestamp': start_date.strftime('%Y-%m-%d %H:%M:%S'),
                'type': workout_type,
                'duration': duration,
                'calories': calories,
                'distance': distance
            })

        except (ValueError, TypeError) as e:
            print(f"Error parsing workout: {e}")

    def parse_file(self, zip_path: str) -> Dict[str, Any]:
        """Main parsing function."""
        try:
            xml_path = self.extract_zip(zip_path)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            # Parse records
            for record in root.findall('.//Record'):
                self.parse_record(record)

            # Parse workouts
            for workout in root.findall('.//Workout'):
                self.parse_workout(workout)

            # Convert to DataFrames for easier aggregation
            dfs = {}
            for key, data in self.records.items():
                if data:
                    dfs[key] = pd.DataFrame(data)
                    if 'date' in dfs[key].columns:
                        dfs[key]['date'] = pd.to_datetime(dfs[key]['date'])

            # Calculate statistics
            stats = self.calculate_statistics(dfs)
            
            return stats

        except Exception as e:
            print(f"Error parsing health data: {e}")
            return {}

    def calculate_statistics(self, dfs: Dict[str, pd.DataFrame]) -> Dict[str, Any]:
        """Calculate various statistics from the parsed data."""
        stats = {
            'total_stats': {},
            'weekly_stats': {},
            'workout_stats': {},
            'heart_stats': {}
        }

        # Total statistics
        if 'steps' in dfs:
            stats['total_stats']['total_steps'] = int(dfs['steps']['value'].sum())
            stats['total_stats']['avg_daily_steps'] = int(dfs['steps'].groupby('date')['value'].sum().mean())

        if 'distance' in dfs:
            stats['total_stats']['total_distance_km'] = round(dfs['distance']['value'].sum() / 1000, 2)
            stats['total_stats']['avg_daily_distance_km'] = round(dfs['distance'].groupby('date')['value'].sum().mean() / 1000, 2)

        if 'active_energy' in dfs:
            stats['total_stats']['total_active_calories'] = int(dfs['active_energy']['value'].sum())
            stats['total_stats']['avg_daily_calories'] = int(dfs['active_energy'].groupby('date')['value'].sum().mean())

        # Workout statistics
        if 'workouts' in dfs:
            workout_df = dfs['workouts']
            stats['workout_stats'] = {
                'total_workouts': len(workout_df),
                'unique_workout_types': list(self.workout_types),
                'most_common_workout': workout_df['type'].mode().iloc[0] if not workout_df.empty else None,
                'total_workout_minutes': round(workout_df['duration'].sum() / 60, 2),
                'avg_workout_duration': round(workout_df['duration'].mean() / 60, 2),
                'total_workout_calories': int(workout_df['calories'].sum()),
                'avg_workout_calories': int(workout_df['calories'].mean())
            }

            # Calculate calories by workout type
            calories_by_type = workout_df.groupby('type').agg({
                'calories': ['sum', 'mean', 'count']
            }).round(2)
            stats['workout_stats']['calories_by_type'] = calories_by_type.to_dict()

        # Heart rate statistics
        if 'heart_rate' in dfs:
            heart_df = dfs['heart_rate']
            stats['heart_stats'] = {
                'avg_heart_rate': round(heart_df['value'].mean(), 2),
                'max_heart_rate': round(heart_df['value'].max(), 2),
                'min_heart_rate': round(heart_df['value'].min(), 2)
            }

        # Weekly statistics
        for metric in ['steps', 'active_energy', 'distance']:
            if metric in dfs:
                weekly_stats = dfs[metric].set_index('date').resample('W')['value'].sum()
                best_week = weekly_stats.idxmax()
                stats['weekly_stats'][f'best_{metric}_week'] = {
                    'week_starting': best_week.strftime('%Y-%m-%d'),
                    'value': round(weekly_stats[best_week], 2)
                }

        return stats

def parse_health_data(zip_path: str) -> Dict[str, Any]:
    """Main function to parse health data."""
    parser = HealthDataParser()
    return parser.parse_file(zip_path)

# Example usage
if __name__ == "__main__":
    # Replace with your zip file path
    zip_file_path = "path_to_your_apple_health_export.zip"
    stats = parse_health_data(zip_file_path)
    print(json.dumps(stats, indent=2))