#!/bin/sh
docker-compose run --rm backend-api ./test.sh "$@"
