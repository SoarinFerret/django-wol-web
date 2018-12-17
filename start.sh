#!/bin/bash

# Apply database migrations
python manage.py makemigrations wol
python manage.py migrate

# Permission issues -.-
chown www-data:www-data /var/www/html -R
chmod a+rw /var/www/html -R

# Collect Static
python manage.py collectstatic --noinput 1> /dev/null

# Start apache2
echo Starting Apache.
/usr/sbin/apache2ctl -DFOREGROUND