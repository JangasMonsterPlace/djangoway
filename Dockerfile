FROM python:3.9-alpine3.13
 
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
# Install dependencies required for psycopg2 python package
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \ 
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev


RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps



RUN mkdir -p /app
COPY ./ ./app
WORKDIR /app
# RUN mv wait-for /bin/wait-for

# RUN pip install --no-cache-dir -r requirements.txt

# # Remove dependencies only required for psycopg2 build
# RUN apk del .build-deps

# EXPOSE 8000

# CMD ["gunicorn", "mysite.wsgi", "0:8000"]