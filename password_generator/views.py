from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def password_generator(request):
    return render(request, 'password_generator/password_home.html')

def about(request):
    return render(request, 'password_generator/about.html')



def password(request):

    thepassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length',12))

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'password_generator/password.html', {'password': thepassword})