#!/bin/sh

set -e

git pull

docker compose \
-f compose.prod.yml \
-f compose.ssl.yml \
pull

docker compose \
-f compose.prod.yml \
-f compose.ssl.yml \
up -d

docker image prune -f
