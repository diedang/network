from django.shortcuts import render,render_to_response
# coding=utf-8
# Create your views here.
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from student.models import Student

# Create your views here.
class UserForm(forms.Form):
    # username = forms.HiddenInput()
    headImg = forms.FileField()

def register(request):
    print request.session['username'], '!!!!!!!!!!!!1'
    username = request.session['username']
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            username = request.session['username']  #uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            user = Student()
            user.username = username
            user.headImg = headImg
            user.save()
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf, 'username':username})