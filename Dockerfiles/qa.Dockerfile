# This dockerfile is used to run, does not work properly with jenkins
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8
RUN apk --update add bash nano
RUN apk add postgresql-dev gcc python3-dev musl-dev postgresql libpq postgresql-client
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
COPY ./instance/qa.config.py /etc/flask/app/qa.config.py
ENV APP_CONFIG_FILE /etc/flask/app/qa.config.py