from django.shortcuts import render
from djangoexample import tools
from django.http import HttpResponse

def fakeid(request):
    iid =request.GET.get("iid")
    fakeid = request.GET.get("fakeid")

    if iid:
        r = tools.myencode(int(iid))
    else:
        r= tools.mydecode(fakeid)
    
    return HttpResponse(r)
