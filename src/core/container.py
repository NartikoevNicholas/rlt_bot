from dependency_injector import (
    containers,
    providers
)

from motor.motor_asyncio import AsyncIOMotorClient

from src.core import get_default_settings
from src.infrastructure.repositories import AggregationDataRepository
from src.services.use_cases import AggregateDataUseCase


settings = get_default_settings()


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "src.handler"
        ]
    )

    mongo_client = providers.Factory(
        AsyncIOMotorClient,
        settings.MONGO.get_uri
    )

    # infrastructure
    employee_repo = providers.Factory(
        AggregationDataRepository,
        client=mongo_client,
        db=settings.MONGO.MONGO_INITDB_DATABASE
    )

    # use_cases
    employee_use_case = providers.Factory(
        AggregateDataUseCase,
        repository=employee_repo

    )
