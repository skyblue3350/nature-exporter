FROM python:3

WORKDIR /opt/app
COPY . .

RUN pip install poetry \
 && poetry install

CMD poetry run python -m nature_exporter
