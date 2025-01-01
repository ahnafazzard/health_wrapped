from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseHealthRecord:
    creation_date: datetime
    start_date: datetime
    end_date: datetime

    def __init__(self, record: dict):
        self.creation_date = datetime.strptime(
            record.get("creationDate"), "%Y-%m-%d %H:%M:%S %z"
        )
        self.start_date = datetime.strptime(
            record.get("startDate"), "%Y-%m-%d %H:%M:%S %z"
        )
        self.end_date = datetime.strptime(record.get("endDate"), "%Y-%m-%d %H:%M:%S %z")


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
    unit: str
    value: float

    def __init__(self, record: dict):
        super().__init__(record)
        self.unit = "step(s)"
        self.value = int(record.get("value"))


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
