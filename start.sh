#!/bin/bash
DOCKER_PORT='56733'
DOCKER_CONTAINER_NAME='docker.test'

while getopts n:p: option; do
	case "${option}" in
		n) DOCKER_CONTAINER_NAME=${OPTARG};;
		p) DOCKER_PORT=${OPTARG};;
	esac
done

docker stop ${DOCKER_CONTAINER_NAME}
docker rm ${DOCKER_CONTAINER_NAME}
docker build -t ${DOCKER_CONTAINER_NAME} .
docker run -d -p ${DOCKER_PORT}:80 --name=${DOCKER_CONTAINER_NAME} -v $PWD:/app ${DOCKER_CONTAINER_NAME}