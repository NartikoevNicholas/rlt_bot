from src.infrastructure.repositories import AbstractAggregationDataRepository
from src.services.entities import (
    AggregateSalaryRequest,
    AggregateSalaryResponse
)
from src.utils.helper import next_date


class AggregateDataUseCase:
    def __init__(self, repository: AbstractAggregationDataRepository):
        self._repo = repository

    async def aggregate_salary(self, schema: AggregateSalaryRequest) -> AggregateSalaryResponse:
        data = {}
        start = schema.dt_from
        date_format = schema.group_type.date_format()
        while schema.dt_upto >= start:
            data[start.strftime(date_format)] = [start.isoformat(), 0]
            start = next_date(start, schema.group_type.value)

        salary_data = await self._repo.get_salary_data(schema)
        for el in salary_data:
            if value := data.get(el.date):
                value[1] = el.value

        aggregate_salary_response = AggregateSalaryResponse()
        for date, value in data.values():
            aggregate_salary_response.dataset.append(value)
            aggregate_salary_response.labels.append(date)

        return aggregate_salary_response
