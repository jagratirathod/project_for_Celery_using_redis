from celery import shared_task
from django.core.mail import send_mail
from celery_with_redis  import settings
from django.contrib.auth import get_user_model


@shared_task(bind = True)
def send_mail_func(self):
    # users = get_user_model().objects.all()
    #timezone.localtime(users.date_time) + timedelta(days=2)

    # for user in users:
    #     mail_subject = "Hi ! Celery Testing"
    #     message = "If you are liking content,please share"
    #     # to_email = user.email
    #     send_mail(
    #         subject = mail_subject ,
    #         message = message ,
    #         from_email = settings.EMAIL_HOST_USER ,
    #         recipient_list= ['jagratirathod02@gmail.com'] ,
    #         fail_silently=True ,
    #     )
    # return "Done" 


    mail_subject = "Hi ! Celery Testing"
    message = "If you are liking content,please share"

    send_mail(
    subject = mail_subject ,
    message = message ,
    from_email = settings.EMAIL_HOST_USER ,
    recipient_list= ['jagratirathod02@gmail.com'] ,
    fail_silently=True ,
    )
    return "Done" 



# pip install django-celery-beat

#  (This three command should run at same time on different terminal)
# terminal -  celery -A  celery_with_redis beat -l INFO
#             celery -A celery_with_redis.celery worker -l  info
#             python manage.py runserver


#  http://localhost:8000/admin/   ->   check ->  Crontabs and Periodic tasks          