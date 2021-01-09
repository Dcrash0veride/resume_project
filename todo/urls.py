from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    path('', views.welcome, name='welcome'),

    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    #ToDos
    path('current/', views.currenttodos, name='currenttodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('<int:todo_pk>/complete/', views.completetodo, name='completetodo'),
    path('<int:todo_pk>/delete/', views.deletetodo, name='deletetodo'),

]