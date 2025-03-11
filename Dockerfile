FROM ghcr.io/hassio-addons/base-python:latest

RUN pip install flask requests

COPY run.py /run.py
CMD ["python3", "/run.py"]
