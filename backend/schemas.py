# schemas.py
from typing import Any, Dict, List, Tuple

from pydantic import BaseModel


class WeeklyStats(BaseModel):
    week: int
    total_steps: int
    start_date: str
    end_date: str


class HealthMetrics(BaseModel):
    total_steps: Tuple[int, str]
    total_distance: Tuple[float, str]
    total_calories: Tuple[float, str]
    average_vo2max: Tuple[float, str]
    weekly_stats: List[WeeklyStats]
    best_week: Dict[str, Any]


class WorkoutMetrics(BaseModel):
    stats_by_type: Dict[str, Any]
    total_calories: Tuple[float, str]


class HealthResponse(BaseModel):
    health: HealthMetrics
    workouts: WorkoutMetrics
