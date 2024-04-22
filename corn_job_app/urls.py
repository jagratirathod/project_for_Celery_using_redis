from django.urls import path
from . import views 

app_name = "corn_job_app"

urlpatterns = [
    path('', views.home),
]