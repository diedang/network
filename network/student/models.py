# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models


# Create your models here.

class ClassRoom(models.Model):
    class_room_name = models.CharField('', max_length=20)
    pass

class Assignment(models.Model):
    class_room = models.ForeignKey(ClassRoom)
    start = None
    end = None
    descri = None


class Student(models.Model):
    class_room = models.ForeignKey(ClassRoom, blank=True, null=True)
    username = models.CharField(u'学号', max_length=20)
    headImg = models.FileField(upload_to = './upload/')
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(u'密码',max_length = 20)
    # @staticmethod
    # def create_student(student_id, password):
    #     # user = User.objects.create_user()
    #     # student = Student()
    #     # student.student_id
    #     # student.user = user
    #     # user.save()
    #     # student.save()
    #     pass

class AssignmentSubmission(models.Model):
    student = models.ForeignKey(Student)
    assignment = models.ForeignKey(Assignment)
    # 上交的文件
    # 上交的时间
    pass

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')

admin.site.register(Student,UserAdmin)