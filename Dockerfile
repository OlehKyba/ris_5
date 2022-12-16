FROM python:3.10-slim

RUN apt-get update && apt-get install -y default-libmysqlclient-dev libpq-dev gcc

WORKDIR /work

COPY ./requirements.txt /work/
RUN pip install -r requirements.txt

COPY ./ris_5 /work/ris_5