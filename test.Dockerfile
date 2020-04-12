# This dockerfile is used to run tests, does not work properly with jenkins
FROM python:3.7-alpine
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt