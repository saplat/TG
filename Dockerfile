FROM python:latest

WORKDIR /src
COPY pip requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src
