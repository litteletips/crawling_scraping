#!/bin/sh

#set -eu
#trap catch ERR
#function catch {
#    ./uwsgi.sh
#}


#until python django_project/manage.py makemigrations nutrition
#do
#  sleep 2
#done

#sleep 10s

until python manage.py makemigrations
do
  sleep 2
done

until python manage.py migrate
do
  sleep 2
done

until python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('super', 'admin@example.com', 'osaki1choume')"
do
  sleep 2
done


#./uwsgi.sh
gunicorn django_project.wsgi -b 0.0.0.0:3031



