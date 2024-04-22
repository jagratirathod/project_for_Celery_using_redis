from celery import shared_task
import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"


@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        user = User.objects.create_user(username=username, email=email, password=password)
        print(user)
    return '{} random users created with success!'.format(total)




# python manage.py runserver                                            (command run on terminal)
# celery -A  <PROJECTNAME>.celery worker -l  info                       (command run on another terminal for redis server)




# Required installation - 

# pip install celery

# pip install redis

# pip install django-celery-results

# pip install django-celery-beat

# sudo apt update

# sudo apt install redis-server

#  sudo systemctl restart redis.service

# sudo systemctl status redis

# redis-cli

# ping


# https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04