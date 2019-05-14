#!/bin/bash
function postgres_ready(){
    python3 $(dirname "$0")/is_postgres_ready.py
}

until postgres_ready; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

python3 manage.py runserver 0.0.0.0:8000
