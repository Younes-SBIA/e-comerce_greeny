FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add python3-dev gcc musl-dev

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app/