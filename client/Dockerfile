FROM bitnami/spark:latest
USER root
WORKDIR /python
RUN apt update && apt install -yq python
COPY requirements.txt /python/requirements.txt
RUN pip install -r requirements.txt
COPY *.py /python/
COPY ./data/* /data