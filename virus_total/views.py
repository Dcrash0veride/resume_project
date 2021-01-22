import requests
import json
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import hashlib
import os
# Create your views here.

def virus_total_home(request):
    if request.method == 'GET':
        return render(request, 'virus_total/home.html')
    else:
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'

        with open('virus_total/secrets.txt') as f:
            apikey = f.read().strip()

        params = {'apikey': apikey}
        root_directory = 'C:\\Users\\dcrash0veride\\PycharmProjects\\resume\\resume\\'
        files = request.FILES['to_check']
        fs = FileSystemStorage()
        name = fs.save(files.name, files)
        ur2 = fs.url(name)
        file_location = root_directory + ur2
        to_pass = {'file': (ur2, open(file_location, 'rb'))}

        response = requests.post(url, files=to_pass, params=params)
        results = response.json()
        resource_id = results['resource']
        url2 = 'https://www.virustotal.com/vtapi/v2/file/report'
        param2 = {'apikey': apikey, 'resource': resource_id}
        response2 = requests.get(url2, params=param2).json()
        av_list = []
        detection = []


        for key in response2['scans'].items():
            av_list.append(key[0])
        for vendor in av_list:
            detection.append(response2['scans'][vendor]['detected'])
        result_dict = {av_list[i]: detection[i] for i in range(len(av_list))}
        return render(request, 'virus_total/success.html', {'result_dict': result_dict})

def get_report(request, resource):
    pass