#!/bin/sh

set -e

git pull

docker compose -f docker-compose.prod.yml pull

docker compose -f docker-compose.prod.yml up -d

docker image prune -f
