FROM python:3 as builder

WORKDIR /opt/app

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY pyproject.toml poetry.lock ./

RUN . /root/.poetry/env && poetry export -f requirements.txt > requirements.txt

FROM python:3-slim

WORKDIR /opt/app
COPY --from=builder /opt/app/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9315
CMD python -u -m nature_exporter
