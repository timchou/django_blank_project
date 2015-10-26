# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve
from django.http import HttpResponse
from djangoexample import consts,tools
from django.shortcuts import redirect
from django.conf import settings
import urllib,os

class DisableCSRF(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        
        FlagC = False
        if FlagC and '/api/v1/' in request.path:
            #对于API的请求，验证
            r = tools.valid_api(request)
            if not r:
                return HttpResponse(content=u"sign error",content_type="application/json", status=401,reason=u"sign error")
