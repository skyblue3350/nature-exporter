import os
import time

import requests
from prometheus_client import start_http_server, Summary

from nature_exporter.metrics.api import metrics as api_metrics
from nature_exporter.metrics.smartmeter import metrics as smartmeter_metrics
from nature_exporter.metrics.remo import metrics as remo_metrics


SMARTMETER_REQUEST_TIME = Summary(
    "smartmeter_request_processing_seconds",
    "Time spent processing applianceses request")
SENSOR_REQUEST_TIME = Summary(
    "sensor_request_processing_seconds",
    "Time spent processing device request")


def get_headers(token):
    return {
        "accept": "application/json",
        "Authorization": "Bearer {}".format(token),
    }


def update_api_info(headers):
    for header in ["x-rate-limit-limit", "x-rate-limit-reset", "x-rate-limit-remaining"]:
        api_metrics[header].set(headers[header])


@SMARTMETER_REQUEST_TIME.time()
def smartmeter_process_request(token):
    res = requests.get("https://api.nature.global/1/appliances", headers=get_headers(token))

    for device in res.json():
        if "smart_meter" in device:
            echonetlite_properties = device["smart_meter"]["echonetlite_properties"]
            for echonetlite_property in echonetlite_properties:
                name = echonetlite_property["name"]
                smartmeter_metrics[name].labels(
                    echonetlite_property["epc"]
                ).set(echonetlite_property["val"])

    update_api_info(res.headers)


@SENSOR_REQUEST_TIME.time()
def sensor_request_process_request(token):
    res = requests.get("https://api.nature.global/1/devices", headers=get_headers(token))

    for device in res.json():
        device_name = device["firmware_version"].split("/")[0]
        if device_name == "Remo":
            for label, metrics in remo_metrics.items():
                if label in device["newest_events"]:
                    metrics.labels(device["name"]).set(device["newest_events"][label]["val"])

    update_api_info(res.headers)


def main(port=9315):
    token = os.environ.get("NATURE_TOKEN", None)
    if token is None:
        raise RuntimeError("Required: NATURE_TOKEN environment")

    print("starting http server port: {}".format(port))
    start_http_server(port)
    while True:
        smartmeter_process_request(token)
        sensor_request_process_request(token)
        time.sleep(20)


if __name__ == "__main__":
    main()
