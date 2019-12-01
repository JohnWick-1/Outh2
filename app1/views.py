from django.shortcuts import render,redirect
from .serializers import *
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
# Create your views here.
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics
from oauth2_provider.views.generic import ProtectedResourceView
from django.http.response import HttpResponse

from .serializers import *
from rest_framework.viewsets import ModelViewSet
import json
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



app_register_url = 'http://localhost:8000/o/applications/'



class StudentViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



def user_login(request):
    if request.method=='POST':
        username,password = request.POST.get('username'),request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                data = {'grant_type': 'password', 'username': username, 'password': password}
                response = requests.post('http://localhost:8000/o/token/', data=data, auth=(clientid, clientsecreat))
                access_token = response.json()['access_token']
                refresh_token = response.json()['refresh_token']
                request.session['data'] = data
                request.session['access_token'] = access_token
                request.session['refresh_token'] = refresh_token
                response = render(request,'login.html',{'msg': 'login successful',
                                    'access_token':access_token,'refresh_token':refresh_token})
                response.set_cookie('headers', {'Authorization': 'Bearer {}'.format(access_token)})

                return response
            return render(request,'login.html',{'msg': 'user not active'})
        else:
            return render(request,'login.html',{'msg': 'invalid credential'})
    else:
        return render(request,'login.html')


@login_required(login_url='http://127.0.0.1:8000/login/')
def user_logout(request):
    logout(request)
    try:
        del request.session['data']
        del request.session['access_token']
        del request.session['refresh_token']
        del request.delete_cookie['headers']
        print(' clear ' * 10)
    finally:
        return render(request,'login.html',{'msg': 'logout successful'})


def registration(request):
    if request.method=='POST':
        username,password = request.POST.get('username'),request.POST.get('password')
        user_mail = request.POST.get('email')
        user = User.objects.create_user(username, user_mail, password)
        user.save()
        return render(request, 'registration.html',{'msg':'{} created'.format(user.username)})
    return render(request, 'registration.html',{'msg':'welcome'})


@login_required(login_url='http://127.0.0.1:8000/login/')
def restricted_stud(request):
    response = requests.get('http://127.0.0.1:8000/v1/student/',
                        headers = {'Authorization': 'Bearer {}'.format(request.session['access_token']),})
    print(response.status_code)
    print(request.session['access_token'])
    print(response.json())
    return HttpResponse('{}'.format(response.json()))



def test(req):
    # req.COOKIES['headers']
    return HttpResponse('{}'.format(req.COOKIES['headers']))








url='http://127.0.0.1:8000/v2/data/'
url2='http://127.0.0.1:8000/v1/student/'
tok='http://localhost:8000/o/token/'
clientid='JK9pr01DhouwZ5e50qjnNCZs4E0nT8anoaYiNIo0'
clientsecreat='R17kVU3lkqLXccqBnfEhDFPlvui3Ortj6xwFshWZNSLhQlElCDlqJEm0IUkdMLFavTQ259n9OM86BwsOvgtMCAITiNUlAANnnXjsWTKekrOj35BzSXeSTuF3f7Ql7cMZ'

clientid2='n6HkMUoKkKEiMgvcH1joLOZWVJ9RvU1ZJa0NfmtH'
clientsecreat2='Rejm4HRRlkjejt8RMAGXDYBpQwqIRZ2gFCjvMm7vZmKlKKKB7jBrm9WmIm45iBhXdKtcdzturnCDz4zp4bvcODNHycIK8LpTSsBQWvbU6yz758IMvAd2IlYoAlV5eyOf'

def method(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        data = {'grant_type':'password','username': username,'password': password}

        response = requests.post('http://localhost:8000/o/token/', data=data,auth=(clientid,clientsecreat))
        access_token=response.json()['access_token']

        headers = {'Authorization': 'Bearer {}'.format(access_token),}

        response1 = requests.get('http://127.0.0.1:8000/v1/student/', headers=headers)
        response2 = requests.get('http://127.0.0.1:8000/v2/data/', headers=headers)
        return render(request,'main.html',context={'app1':json.loads(response1.json()),'app2':json.loads(response2)})
    return render(request,'main.html')

