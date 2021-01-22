from django.urls import path
from . import views


app_name = 'virus_total'

urlpatterns = [
    path('', views.virus_total_home, name='virus_total_home'),
]