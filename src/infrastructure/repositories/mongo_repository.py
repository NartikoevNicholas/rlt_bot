from typing import List

from src.services.entities import (
    AggregateSalaryData,
    AggregateSalaryRequest,
)

from .abstract import (
    AbstractAggregationDataRepository,
    MongoDBAdapter
)


class AggregationDataRepository(AbstractAggregationDataRepository, MongoDBAdapter):
    async def get_salary_data(self, schema: AggregateSalaryRequest) -> List[AggregateSalaryData]:
        collection = self._db['sample_collection']
        pipeline = [
            {'$match': {'dt': {'$gte': schema.dt_from, '$lte': schema.dt_upto}}},
            {'$group': {
                '_id': {'$dateToString': {'format': schema.group_type.date_format(), 'date': '$dt'}},
                'value': {'$sum': '$value'}
            }},
        ]
        data = []
        async for el in collection.aggregate(pipeline):
            data.append(AggregateSalaryData(date=el['_id'], value=el['value']))
        return data
