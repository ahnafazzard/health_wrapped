from datetime import datetime
from itertools import groupby
from operator import itemgetter
from typing import Any, Dict, List, Tuple

from health_models import (
    ActiveEnergyBurnedRecord,
    DistanceWalkingRunningRecord,
    StepCountRecord,
    VO2MaxRecord,
)


class HealthRecords:
    def __init__(self, health_data: Dict[str, Any]):
        self.records: List[Dict[str, str]] = health_data.get("Record", {})

        self.DistanceWalkingRunning_records = list(
            map(
                DistanceWalkingRunningRecord,
                filter(
                    lambda x: x["type"]
                    == "HKQuantityTypeIdentifierDistanceWalkingRunning",
                    self.records,
                ),
            )
        )

        self.StepCount_records = list(
            map(
                StepCountRecord,
                filter(
                    lambda x: x["type"] == "HKQuantityTypeIdentifierStepCount",
                    self.records,
                ),
            )
        )

        self.VO2Max_records = list(
            map(
                VO2MaxRecord,
                filter(
                    lambda x: x["type"] == "HKQuantityTypeIdentifierVO2Max",
                    self.records,
                ),
            )
        )

        self.ActiveEnergyBurned_records = list(
            map(
                ActiveEnergyBurnedRecord,
                filter(
                    lambda x: x["type"] == "HKQuantityTypeIdentifierActiveEnergyBurned",
                    self.records,
                ),
            )
        )

    def _filter_records_by_year(
        self, records: List[Any], year: int = datetime.now().year
    ) -> List[Any]:
        if not year:
            year = datetime.now().year
        return [record for record in records if record.start_date.year == year]

    def get_total_steps_for_year(
        self, year: int = datetime.now().year
    ) -> Tuple[int, str]:
        yearly_records = self._filter_records_by_year(self.StepCount_records, year)
        unit = set(yearly_record.unit for yearly_record in yearly_records)
        if len(unit) > 1:
            raise ValueError("Multiple units found")
        unit = unit.pop()
        return sum(int(record.value) for record in yearly_records), unit

    def get_total_distance_for_year(
        self, year: int = datetime.now().year
    ) -> Tuple[float, str]:
        yearly_records = self._filter_records_by_year(
            self.DistanceWalkingRunning_records, year
        )
        unit = set(yearly_record.unit for yearly_record in yearly_records)
        if len(unit) > 1:
            raise ValueError("Multiple units found")
        unit = unit.pop()
        return round(sum(float(record.value) for record in yearly_records), 2), unit

    def get_total_calories_for_year(
        self, year: int = datetime.now().year
    ) -> Tuple[float, str]:
        yearly_records = self._filter_records_by_year(
            self.ActiveEnergyBurned_records, year
        )
        unit = set(yearly_record.unit for yearly_record in yearly_records)
        if len(unit) > 1:
            raise ValueError("Multiple units found")
        unit = unit.pop()
        return round(sum(float(record.value) for record in yearly_records), 2), unit

    def get_average_vo2max(self, year: int = datetime.now().year) -> Tuple[float, str]:
        yearly_records = self._filter_records_by_year(self.VO2Max_records, year)
        if not yearly_records:
            return 0.0
        unit = set(yearly_record.unit for yearly_record in yearly_records)
        if len(unit) > 1:
            raise ValueError("Multiple units found")
        unit = unit.pop()
        return (
            round(
                sum(float(record.value) for record in yearly_records)
                / len(yearly_records),
                2,
            ),
            unit,
        )

    def get_stats_by_week(self, year: int = datetime.now().year) -> List[Dict]:
        steps = self._filter_records_by_year(self.StepCount_records, year)

        # Group by week number
        def get_week(record):
            # date = datetime.strptime(record.start_date, "%Y-%m-%d %H:%M:%S %z")
            # return date.isocalendar()[1]
            return record.start_date.isocalendar()[1]

        weekly_stats = []
        for week, records in groupby(sorted(steps, key=get_week), key=get_week):
            records_list = list(records)
            total_steps = sum(int(record.value) for record in records_list)
            weekly_stats.append(
                {
                    "week": week,
                    "total_steps": total_steps,
                    "start_date": min(r.start_date for r in records_list),
                    "end_date": max(r.end_date for r in records_list),
                }
            )

        return weekly_stats

    def get_best_week(self, year: int = datetime.now().year) -> Dict:
        weekly_stats = self.get_stats_by_week(year)
        if not weekly_stats:
            return {}
        return max(weekly_stats, key=itemgetter("total_steps"))


if __name__ == "__main__":

    import json

    with open("sample_data/export.json", "r") as f:
        health_data_sample = json.load(f)

    records = HealthRecords(health_data_sample)

    year = 2024

    weekly_stats_l = records.get_stats_by_week(year=year)
    weekly_stats_l = list(
        map(
            lambda x: {
                k: v.strftime("%Y-%m-%d") if isinstance(v, datetime) else v
                for k, v in x.items()
            },
            weekly_stats_l,
        )
    )
    best_week = records.get_best_week(year=year)
    best_week = {
        k: v.strftime("%Y-%m-%d") if isinstance(v, datetime) else v
        for k, v in best_week.items()
    }

    d = {
        f"get_total_steps_for_year_{year}": " ".join(
            map(str, records.get_total_steps_for_year(year=year))
        ),
        f"get_total_distance_for_year_{year}": " ".join(
            map(str, records.get_total_distance_for_year(year=year))
        ),
        f"get_total_calories_for_year_{year}": " ".join(
            map(str, records.get_total_calories_for_year(year=year))
        ),
        f"get_average_vo2max_{year}": " ".join(
            map(str, records.get_average_vo2max(year=year))
        ),
        f"get_stats_by_week_{year}": weekly_stats_l,
        f"get_best_week_{year}": best_week,
    }

    output = json.dumps(d, indent=2, ensure_ascii=False)

    print(output)

    with open("logfiles/test_health_records_log.json", "w") as f:
        f.write(output)
