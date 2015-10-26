# -*- coding: utf-8 -*-
import os,sys,datetime,requests,json,time,re
from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoexample.settings'
application = get_wsgi_application()

from django.db import transaction
from django.db.models import Q
from django.db import transaction
from django.contrib.auth.models import User
from django.conf import settings
from djangoexample.settings import log_crontab

def hello():
    log_crontab.info("now ....")
    print u"hello world你好"

if __name__ == '__main__':
    hello()
