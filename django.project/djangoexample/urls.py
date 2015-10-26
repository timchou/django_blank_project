# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
import apps

router = routers.DefaultRouter()

urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #main view
    url(r'^$', 'djangoexample.views.home', name='home'),
    url(r'^misc/fakeid/$', 'apps.miscs.views.fakeid'),
)
