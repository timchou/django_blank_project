# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import transaction
import json,datetime,operator,requests,urllib
from django.contrib import auth
from django.core.cache import cache
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.datastructures import MultiValueDict
from djangoexample import tools,consts
from rest_framework.parsers import JSONParser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.users.models import UserProfile

def web_sina_login(request):
    context={
        'request'   :request,
    }

    return render(request, 'backend/login.html', context)

