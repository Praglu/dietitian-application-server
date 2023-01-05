#!/bin/sh

set -o errexit
set -o nounset

# We need this line to make sure that this container is started
# after the one with postgres:
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Migrating database..."
python /code/manage.py migrate --noinput

echo "Compile translations..."
python /code/manage.py compilemessages

cd /code
python manage.py runserver 0.0.0.0:8000

/usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
