#!/bin/sh

docker compose \
-f compose.prod.yml \
-f compose.ssl.yml \
run --rm certbot \
certonly \
--webroot \
-w /var/www/certbot \
-d noteflow.prs2rnn.tech \
--email vederecento@gmail.com \
--agree-tos \
--no-eff-email
