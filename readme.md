#To install requirements:

######1. install redis server (https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)
######Be sure of installation by following command:
####### sudo systemctl status redis
######=> Active: active (running)
######2. pip3 install celery
######3. pip3 install redis


#To Run The Django Server Do the Followings in Terminal:

######python3 manage.py makemigrations
######python3 manage.py migrate
######python3 manage.py runserver


#To Run The Celery Worker Do the Followings in Terminal:
######celery -A NetLab.celery worker --loglevel=info
