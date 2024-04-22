from .models import Widget
import random 

def print_hello():
    number=random.randint(0,100)
    Widget.objects.create(font_size=number)
    


# pip install django-crontab

# python manage.py crontab add

# python manage.py crontab show

# python manage.py runserver