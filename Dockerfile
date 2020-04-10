FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.8
COPY ./requirements.txt /var/www/requirements.txt