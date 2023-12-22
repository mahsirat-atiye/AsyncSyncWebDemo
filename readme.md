NetLab project which is showcasing the difference between synchronous (blocking) and asynchronous (non-blocking) tasks in a web application.
#### Install requirements:

1. install [redis server](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)
Make sure of installation by following command:
```
 sudo systemctl status redis
```
The result should be active
2. install requirements

```
pip3 install pip install -r requirements.txt
```


#### Run The Django Server:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```


#### Run The Celery Worker:
```
celery -A NetLab.celery worker --loglevel=info
```
