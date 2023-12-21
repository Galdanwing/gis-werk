#!/bin/bash

set -e
cmd="$@"
until python manage.py migrate; do
  sleep 2
  echo "Postgres not alive, Retry!";
done
python manage.py runserver 0.0.0.0:8000


exec $cmd
