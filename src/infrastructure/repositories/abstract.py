from abc import (
    ABC,
    abstractmethod
)

from typing import List

from motor.motor_asyncio import AsyncIOMotorClient

from src.services.entities import (
    AggregateSalaryData,
    AggregateSalaryRequest
)


class AbstractRepository(ABC):
    ...
    """
    Тут должны быть дефолтные методы CRUD(insert, select, patch, delete), но тк в них 
    нет необходимости я их не добавил. Может показаться, что этот класс излишний.
    """


class AbstractAggregationDataRepository(AbstractRepository, ABC):
    @abstractmethod
    async def get_salary_data(self, schema: AggregateSalaryRequest) -> List[AggregateSalaryData]:
        raise NotImplementedError


class MongoDBAdapter(AbstractRepository):

    def __init__(self, client: AsyncIOMotorClient, db: str):
        self._client = client
        self._db = client[db]

    """
    Тут должны быть реализованны дефолтные методы из абстрактного класса (AbstractRepository)
    """