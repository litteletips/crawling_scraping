#!/bin/bash

#DIR=/usr/src/app/django_project/nutrition/migrations

if [[ -d /usr/src/app/django_project/nutrition/migrations ]]; then
    ./uwsgi.sh
else
    ./setup.sh
    ./uwsgi.sh
fi
