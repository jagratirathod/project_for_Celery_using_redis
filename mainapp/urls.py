from django.urls import path
from . import views 

app_name = "mainapp"

urlpatterns = [
    path('test/', views.test),
    path('', views.GenerateRandomUserView.as_view(),name="generate"),    
]