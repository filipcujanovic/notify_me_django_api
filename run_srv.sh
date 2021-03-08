#!/bin/env bash

cd /var/www/html/friends/apps/notify-me/notify_me_django_api;

pipenv run python manage.py runserver 0.0.0.0:8001 2>&1 >> /var/log/notify-me/srv.log
