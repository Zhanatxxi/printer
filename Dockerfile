FROM python:3.10.13-alpine3.18

WORKDIR /app

COPY requirements.txt .

RUN  apt-get update && pip install -r requirements.txt

COPY . /app

CMD ['python', 'api.py']
