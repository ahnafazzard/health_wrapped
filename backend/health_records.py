from typing import Any, Dict

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


if __name__ == "__main__":
    health_data = {
        "Record": [
            {
                "type": "HKQuantityTypeIdentifierDistanceWalkingRunning",
                "sourceName": "Mushfiqur's iPhone",
                "sourceVersion": "15.0",
                "device": "<<HKDevice: 0x301b13ca0>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone12,3, software:15.0, creation date:2021-09-22 17:33:35 +0000>",
                "unit": "km",
                "creationDate": "2021-10-13 06:52:09 -0500",
                "startDate": "2021-10-13 06:39:32 -0500",
                "endDate": "2021-10-13 06:49:32 -0500",
                "value": "0.0804713",
            },
            {
                "type": "HKQuantityTypeIdentifierDistanceWalkingRunning",
                "sourceName": "Mushfiqur's iPhone",
                "sourceVersion": "15.0",
                "device": "<<HKDevice: 0x301b13ca0>, name:iPhone, manufacturer:Apple Inc., model:iPhone, hardware:iPhone12,3, software:15.0, creation date:2021-09-22 17:33:35 +0000>",
                "unit": "km",
                "creationDate": "2021-10-13 07:02:07 -0500",
                "startDate": "2021-10-13 06:51:05 -0500",
                "endDate": "2021-10-13 06:54:18 -0500",
                "value": "0.0287828",
            },
            {
                "type": "HKQuantityTypeIdentifierStepCount",
                "sourceName": "Mushfiqur\u2019s Apple\u00a0Watch",
                "sourceVersion": "8.0",
                "device": "<<HKDevice: 0x301b11310>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,1, software:8.0, creation date:2021-09-25 06:03:07 +0000>",
                "unit": "count",
                "creationDate": "2021-10-14 05:52:39 -0500",
                "startDate": "2021-10-14 05:40:38 -0500",
                "endDate": "2021-10-14 05:50:39 -0500",
                "value": "207",
            },
            {
                "type": "HKQuantityTypeIdentifierStepCount",
                "sourceName": "Mushfiqur\u2019s Apple\u00a0Watch",
                "sourceVersion": "8.0",
                "device": "<<HKDevice: 0x301b11310>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,1, software:8.0, creation date:2021-09-25 06:03:07 +0000>",
                "unit": "count",
                "creationDate": "2021-10-14 06:02:36 -0500",
                "startDate": "2021-10-14 05:52:09 -0500",
                "endDate": "2021-10-14 06:01:40 -0500",
                "value": "419",
            },
            {
                "type": "HKQuantityTypeIdentifierVO2Max",
                "sourceName": "Mushfiqur\u2019s Apple\u00a0Watch",
                "sourceVersion": "2663.1.1",
                "unit": "mL/min\u00b7kg",
                "creationDate": "2021-10-12 16:39:43 -0500",
                "startDate": "2021-10-12 16:39:43 -0500",
                "endDate": "2021-10-12 16:39:43 -0500",
                "value": "38.57",
                "MetadataEntry": [
                    {"key": "HKVO2MaxTestType", "value": "2"},
                    {"key": "HKMetadataKeySyncVersion", "value": "1"},
                    {
                        "key": "HKMetadataKeySyncIdentifier",
                        "value": "1A4C8486-A435-4192-8492-BD41E63BB6FC",
                    },
                ],
            },
            {
                "type": "HKQuantityTypeIdentifierVO2Max",
                "sourceName": "Mushfiqur\u2019s Apple\u00a0Watch",
                "sourceVersion": "2664.0.8.1.1",
                "unit": "mL/min\u00b7kg",
                "creationDate": "2021-10-31 14:23:53 -0500",
                "startDate": "2021-10-31 14:23:52 -0500",
                "endDate": "2021-10-31 14:23:52 -0500",
                "value": "39.14",
                "MetadataEntry": [
                    {"key": "HKVO2MaxTestType", "value": "2"},
                    {"key": "HKMetadataKeySyncVersion", "value": "1"},
                    {
                        "key": "HKMetadataKeySyncIdentifier",
                        "value": "332884B7-202B-410F-9587-837DC7DB32F3",
                    },
                ],
            },
            {
                "type": "HKQuantityTypeIdentifierActiveEnergyBurned",
                "sourceName": "Mushfiqur\u2019s Apple\u00a0Watch",
                "sourceVersion": "8.0",
                "device": "<<HKDevice: 0x301b10dc0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,1, software:8.0, creation date:2021-09-25 06:03:07 +0000>",
                "unit": "Cal",
                "creationDate": "2021-10-13 22:23:32 -0500",
                "startDate": "2021-10-13 22:20:30 -0500",
                "endDate": "2021-10-13 22:21:31 -0500",
                "value": "0.45",
            },
            {
                "type": "HKQuantityTypeIdentifierActiveEnergyBurned",
                "sourceName": "Mushfiqur\u2019s Apple\u00a0Watch",
                "sourceVersion": "8.0",
                "device": "<<HKDevice: 0x301b10dc0>, name:Apple Watch, manufacturer:Apple Inc., model:Watch, hardware:Watch6,1, software:8.0, creation date:2021-09-25 06:03:07 +0000>",
                "unit": "Cal",
                "creationDate": "2021-10-13 22:23:32 -0500",
                "startDate": "2021-10-13 22:21:31 -0500",
                "endDate": "2021-10-13 22:22:33 -0500",
                "value": "0.414",
            },
        ]
    }

    records = HealthRecords(health_data)
    print(records.DistanceWalkingRunning_records)
    print(records.StepCount_records)
    print(records.VO2Max_records)
    print(records.ActiveEnergyBurned_records)
