from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule

# Create your views here.


def homes(request):
    return HttpResponse("check.....")



def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")


def schedule_mail(request):
    # Dynamically schedule time
    try:
        schedule, created = CrontabSchedule.objects.get_or_create(hour = 14, minute = 54)
        task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task54"+"5", task='celery_beat_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
        return HttpResponse("Done")
    except:
        return HttpResponse("Name should be unique")


