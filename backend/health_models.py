from dataclasses import dataclass
from datetime import datetime


@dataclass
class DistanceWalkingRunningRecord:
    # "unit": "km",
    unit: str
    # "creationDate": "2021-10-13 06:52:09 -0500",
    creationDate: datetime
    # "startDate": "2021-10-13 06:39:32 -0500",
    startDate: datetime
    # "endDate": "2021-10-13 06:49:32 -0500",
    endDate: datetime
    # "value": "0.0804713"
    value: float

    def __init__(self, record: dict):
        self.unit = record.get("unit")
        self.creationDate = datetime.strptime(
            record.get("creationDate"), "%Y-%m-%d %H:%M:%S %z"
        )
        self.startDate = datetime.strptime(
            record.get("startDate"), "%Y-%m-%d %H:%M:%S %z"
        )
        self.endDate = datetime.strptime(record.get("endDate"), "%Y-%m-%d %H:%M:%S %z")
        self.value = float(record.get("value"))


class StepCountRecord:
    # "creationDate": "2021-10-13 06:52:09 -0500",
    creationDate: datetime
    # "startDate": "2021-10-13 06:39:32 -0500",
    startDate: datetime
    # "endDate": "2021-10-13 06:49:32 -0500",
    endDate: datetime
    # "count": "207"
    count: int

    def __init__(self, record: dict):
        self.creationDate = datetime.strptime(
            record.get("creationDate"), "%Y-%m-%d %H:%M:%S %z"
        )
        self.startDate = datetime.strptime(
            record.get("startDate"), "%Y-%m-%d %H:%M:%S %z"
        )
        self.endDate = datetime.strptime(record.get("endDate"), "%Y-%m-%d %H:%M:%S %z")
        self.count = int(record.get("value"))
