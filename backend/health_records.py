from typing import Any, Dict

from health_models import DistanceWalkingRunningRecord, StepCountRecord


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

        # self.VO2Max_records = filter(
        #     lambda x: x["type"] == "HKQuantityTypeIdentifierVO2Max", self.records
        # )

        # self.ActiveEnergyBurned_records = filter(
        #     lambda x: x["type"] == "HKQuantityTypeIdentifierActiveEnergyBurned",
        #     self.records,
        # )
