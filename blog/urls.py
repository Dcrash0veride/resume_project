from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('<int:blog_pk>/delete/', views.deletepost, name='deletepost'),
]