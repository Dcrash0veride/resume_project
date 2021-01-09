from django.urls import path
from portfolio import views


urlpatterns = [
    path('', views.portfolio_home, name='portfolio_home'),
]