# Pics
Example project

## In project were used
Django, DRF, celery, docker-compose, gunicorn, postgres, rabbitmq

## Install:
```bash
git clone https://github.com/i-k-i/pics.git
cd pics
docker-compose up -d
docker-compose run web python manage.py migrate
```
## Using
```browse http://127.0.0.1:8000
```

