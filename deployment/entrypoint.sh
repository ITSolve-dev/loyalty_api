#!/bin/bash
figlet -ct  "Run migrations"
pipenv run migrate
figlet -ct  "Complete migrations"

figlet -ct "Run app server"
exec pipenv run uvicorn main:app --host $SERVER__HOST --port $SERVER__PORT --workers $SERVER__WORKERS

echo "service not found, patch deploy to debug mode"
exit
