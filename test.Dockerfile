# This dockerfile is used to run tests, does not work properly with jenkins
FROM python:3.7-alpine
COPY ./ /var/www/
RUN touch test.txt
RUN touch /var/www/othertest.txt
RUN pip3 install -r /var/www/requirements.txt