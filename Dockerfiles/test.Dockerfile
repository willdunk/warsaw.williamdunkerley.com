# This dockerfile is used to run tests, does not work properly with jenkins
FROM python:3.6-alpine
RUN apk add postgresql-dev gcc python3-dev musl-dev postgresql libpq postgresql-client
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt