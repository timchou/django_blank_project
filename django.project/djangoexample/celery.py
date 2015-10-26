# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoexample.settings')
from django.conf import settings
app = Celery('djangoexample',broker=settings.BROKER_URL)
