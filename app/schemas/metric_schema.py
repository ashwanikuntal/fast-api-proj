from pydantic import BaseModel
from typing import List
from _datetime import datetime

class Metric(BaseModel):
    created_time: datetime
    voltage: int
    current: int


class MetricsData(BaseModel):
    metric: List[Metric]

    class Config:
        orm_mode = True