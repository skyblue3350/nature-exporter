FROM python:3-slim as builder

WORKDIR /opt/app

RUN apt update -y && apt install gcc -y && pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt > requirements.txt

FROM python:3-slim

WORKDIR /opt/app
COPY --from=builder /opt/app/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9315
CMD python -u -m nature_exporter
