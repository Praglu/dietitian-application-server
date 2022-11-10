#!/bin/sh
set -e
docker-compose stop
docker-compose rm -svf
docker volume list | egrep 'dietitian-application-server_.+data' | awk '{ print $2 }' | xargs docker volume rm
docker images | egrep 'dietitian-application-server_.+' | awk '{ print $1 }' | xargs docker rmi -f
rm envs/.docker.env
