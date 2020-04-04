#!/bin/sh

#postfix start

#/root/anaconda3/bin/uwsgi --master --close-on-exec \
#  --socket ${HOSTNAME}:3031  \
#  --processes 2 \
#  --buffer-size=32768 \
#  --workers=5 \
#  --callable=app \
#  --wsgi-file /usr/src/app/backend/app.py #\
#  #--wsgi-file /usr/src/app/django_project/django_project/wsgi.py #\
## &

#/root/anaconda3/bin/uwsgi --master \
#  --http-socket  ${HOSTNAME}:3032 \
#  --wsgi-file /usr/src/app/django_project/django_project/wsgi_websocket.py \
#  --gevent 1000 \
#  --http-websockets \
#  --workers=2
#  #--virtualenv /path/to/virtualenv \
#  --module wsgi_websocket


/root/anaconda3/bin/uwsgi --master --close-on-exec \
  --socket ${HOSTNAME}:3031  \
  --processes 2 \
  --buffer-size=32768 \
  --workers=5 \
  --wsgi-file /usr/src/app/django_project/django_project/wsgi.py