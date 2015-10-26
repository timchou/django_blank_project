# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def home(request):
    return HttpResponse("hello world")
