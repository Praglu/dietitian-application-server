#!/bin/bash
set -e
cp -n envs/docker-env-default envs/.docker.env

sed -i 's/production/development/g' requirements.txt

docker-compose build
docker-compose up --no-start
