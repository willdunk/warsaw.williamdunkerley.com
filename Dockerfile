FROM python:3.7-stretch
RUN apk --update add bash nano
COPY ./requirements.txt /var/www/requirements.txt