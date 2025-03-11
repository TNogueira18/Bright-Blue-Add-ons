ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM $BUILD_FROM

ENV LANG C.UTF-8
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2

# Install dependencies
RUN apk add --no-cache python3 py3-pip

# Install required Python packages
RUN pip3 install flask requests

# Copy the main Python script
COPY run.py /run.py

# Run the application
CMD ["python3", "/run.py"]
