FROM python:3.11-alpine

RUN apk update && apk add --no-cache make

WORKDIR /app
COPY . /app/

RUN pip3 install --upgrade pip && pip3 install poetry
RUN poetry install

CMD poetry run python -m src.main
