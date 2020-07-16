python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver


=====
pip3 install celery
pip3 install redis

======
install redis (https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)

sudo systemctl status redis
=> Active: active (running)

==========
celery -A NetLab.celery worker --loglevel=info
