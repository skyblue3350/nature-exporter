from prometheus_client import Gauge

metrics = {
    "hu": Gauge("humidity", "humidity", ["device_name"]),
    "il": Gauge("illumination", "illumination", ["device_name"]),
    "mo": Gauge("movement", "movement", ["device_name"]),
    "te": Gauge("temperature", "temperature", ["device_name"]),
}
