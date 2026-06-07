#!/bin/sh

docker compose \
-f compose.prod.yml \
-f compose.ssl.yml \
logs -f
