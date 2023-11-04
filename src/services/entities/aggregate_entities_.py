import datetime

from typing import List

from enum import Enum

from pydantic import (
    BaseModel,
    Field
)


class AggregateSalaryData(BaseModel):
    date: str
    value: int


class GroupType(str, Enum):
    hour = 'hour'
    day = 'day'
    week = 'week'
    month = 'month'

    def date_format(self) -> str:
        if self.value == self.hour: return '%Y-%m-%dT%H'
        elif self.value == self.day: return '%Y-%m-%d'
        elif self.value == self.week: return '%Y-%U'
        else: return '%Y-%m'


class AggregateSalaryRequest(BaseModel):
    dt_from: datetime.datetime
    dt_upto: datetime.datetime
    group_type: GroupType


class AggregateSalaryResponse(BaseModel):
    dataset: List[int] = Field(default=[])
    labels: List = Field(default=[])
