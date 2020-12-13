import os

from nature_exporter.cli import main


if __name__ == "__main__":
    token = os.environ.get("NATURE_TOKEN", None)
    port = int(os.environ.get("NATURE_PORT", 9315))
    main(token, port)
