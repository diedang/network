"""network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import student.views
import assignment.views
import home.views

admin.autodiscover()
urlpatterns = [
    # url(r'^courses/', article.views.index),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^secadmin!!!/', admin.site.urls),
    url(r'^$', home.views.index, name='index'),
    # url(r'^news/(?P<col>[^/]+)/$', article.views.list_column,name='column'),
    # url(r'^news/(?P<col>[^/]+)/(?P<art>[^/]+)/$', article.views.show_article,name='article'),
    url(r'^login/$', student.views.login,name='log-in'),
    url(r'^assignment/', assignment.views.register),
    url(r'^page/(?P<col>[^/]+)/$', home.views.static_page, name='page-list'),
    url(r'^page/(?P<col>[^/]+)/(?P<art>[^/]+)/$', home.views.static_page, name='page-show'),


]
