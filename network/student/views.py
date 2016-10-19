# coding=utf-8
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
# Create your views here.
from student.models import Student
from django.contrib.auth import authenticate, login
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='学号:', max_length = 100)
    password = forms.CharField(label='密码:', max_length = 100)
def login_page_show():

    pass

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = Student.objects.filter(username__exact = username,password__exact = password)
            if user:
                request.session['username'] = username
                return render_to_response('success.html',{'username':username})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})
def login_page_callback(request):

    username = ''
    password = ''

    student = Student()

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user);
    else:
        pass

    pass


def register_page_show():
    pass

def register_page_callback():


    pass

