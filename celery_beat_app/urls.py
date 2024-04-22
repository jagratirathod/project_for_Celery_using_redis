from django.urls import path
from . import views 

app_name = "celery_beat_app"

urlpatterns = [
    path('home/', views.homes),
    path('sendmail/', views.send_mail_to_all, name="sendmail"),
    path('schedulemail/', views.schedule_mail, name="schedulemail"),

]

