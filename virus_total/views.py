import requests
import json
import time
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import hashlib
import os
from pathlib import Path
# Create your views here.

def virus_total_home(request):
    if request.method == 'GET':
        return render(request, 'virus_total/home.html')
    else:
        try:
            url = 'https://www.virustotal.com/vtapi/v2/file/scan'

            with open('virus_total/secrets.txt') as f:
                apikey = f.read().strip()

            params = {'apikey': apikey}
            root_directory = Path(__file__).resolve().parent.parent
            files = request.FILES['to_check']
            fs = FileSystemStorage()
            name = fs.save(files.name, files)
            ur2 = fs.url(name)
            file_location = str(root_directory) + ur2
            to_pass = {'file': (ur2, open(file_location, 'rb'))}

            response = requests.post(url, files=to_pass, params=params)
            results = response.json()
            resource_id = results['resource']
            time.sleep(60)
            url2 = 'https://www.virustotal.com/vtapi/v2/file/report'
            param2 = {'apikey': apikey, 'resource': resource_id}
            response2 = requests.get(url2, params=param2).json()
            av_list = []
            detection = []



            try:
                for key in response2['scans'].items():
                    av_list.append(key[0])
                for vendor in av_list:
                    detection.append(response2['scans'][vendor]['detected'])
                result_dict = {av_list[i]: detection[i] for i in range(len(av_list))}
                return render(request, 'virus_total/success.html', {'result_dict': result_dict})
            except (KeyError):
                time.sleep(60)
                for key in response2['scans'].items():
                    av_list.append(key[0])
                for vendor in av_list:
                    detection.append(response2['scans'][vendor]['detected'])
                result_dict = {av_list[i]: detection[i] for i in range(len(av_list))}
                return render(request, 'virus_total/success.html', {'result_dict': result_dict})
        except (FileNotFoundError, MultiValueDictKeyError):
                return render(request, 'virus_total/home.html', {'error': 'file not found, is it empty?'})
