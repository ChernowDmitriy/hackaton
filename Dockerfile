FROM python:3.9

WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
