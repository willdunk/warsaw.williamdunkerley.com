FROM python:3.6-alpine
RUN apk --update add bash nano
RUN apk add postgresql-dev gcc python3-dev musl-dev postgresql libpq postgresql-client build-base linux-headers pcre-dev uwsgi
COPY ./requirements.txt /etc/flask/app/requirements.txt
RUN pip install -r /etc/flask/app/requirements.txt
COPY ./instance/test.config.py /etc/flask/app/test.config.py
ENV APP_CONFIG_FILE /etc/flask/app/test.config.py