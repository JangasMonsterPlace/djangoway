# Dockerfile
FROM python:latest
RUN pip install pipenv
RUN mkdir /code
WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.txt 

