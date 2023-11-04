import json

from aiogram import (
    Router,
    types as tp
)

from dependency_injector.wiring import Provide, inject

from src.core.container import Container
from src.services.use_cases import AggregateDataUseCase
from src.services.entities import AggregateSalaryRequest


router = Router(name='echo')


@router.message()
@inject
async def echo_handler(
    message: tp.Message,
    employee_use_case: AggregateDataUseCase = Provide[Container.employee_use_case]
) -> None:
    try:
        data = AggregateSalaryRequest(**json.loads(message.text))
        dataset = await employee_use_case.aggregate_salary(data)
        await message.answer(json.dumps(dataset.model_dump()))
    except Exception as e:
        await message.answer("Bad request")
        raise e
