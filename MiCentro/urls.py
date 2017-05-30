#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'micentro'
urlpatterns = [
               url(r'^login', views.login_view, name='login'),
               url(r'^home', views.home, name='home')
               ]
