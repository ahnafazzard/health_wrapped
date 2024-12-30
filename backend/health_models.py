from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseHealthRecord:
    creationDate: datetime
    startDate: datetime
    endDate: datetime

    def __init__(self, record: dict):
        self.creationDate = datetime.strptime(
            record.get("creationDate"), "%Y-%m-%d %H:%M:%S %z"
        )
        self.startDate = datetime.strptime(
            record.get("startDate"), "%Y-%m-%d %H:%M:%S %z"
        )
        self.endDate = datetime.strptime(record.get("endDate"), "%Y-%m-%d %H:%M:%S %z")


@dataclass
class DistanceWalkingRunningRecord(BaseHealthRecord):
    unit: str
    value: float

    def __init__(self, record: dict):
        super().__init__(record)
        self.unit = record.get("unit")
        self.value = float(record.get("value"))


@dataclass
class StepCountRecord(BaseHealthRecord):
    count: int

    def __init__(self, record: dict):
        super().__init__(record)
        self.count = int(record.get("value"))


@dataclass
class VO2MaxRecord(BaseHealthRecord):
    unit: str
    value: float

    def __init__(self, record: dict):
        super().__init__(record)
        self.unit = record.get("unit")
        self.value = float(record.get("value"))


@dataclass
class ActiveEnergyBurnedRecord(BaseHealthRecord):
    unit: str
    value: float

    def __init__(self, record: dict):
        super().__init__(record)
        self.unit = record.get("unit")
        self.value = float(record.get("value"))
