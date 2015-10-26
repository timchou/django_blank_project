# -*- coding: utf-8 -*-
from django import template
from djangoexample import opaque,consts

register = template.Library()

@register.filter
def mymulti(value,arg):
    return  value * arg

@register.filter
def myencode(myid):
    encoder = opaque.OpaqueEncoder(consts.IDKEY)
    return encoder.encode_hex(myid)

@register.filter
def display_datetime(event):
    '''
    如果yyyy\mm\dd是一样的，则显示类似2015-6-12(周三) 13:30~14:30
    如果不一样，则显示类似2015-6-12 13:30 - 2015
    '''

    start = event.start
    end   = event.end

    s=""
    if start.year == end.year and start.month == end.month and start.day == end.day:
        w = start.strftime("%w")
        ws=u"周一"
        if w == '2':
            ws = u"周二"
        elif w == '3':
            ws = u"周三"
        elif w == '4':
            ws = u"周四"
        elif w == '5':
            ws = u"周五"
        elif w == '6':
            ws = u"周六"
        elif w == '0':
            ws = u"周日"

        s = "%s(%s) %s ~ %s" % ( start.strftime("%Y-%m-%d") , ws ,start.strftime("%H:%M") , end.strftime("%H:%M"))
    else:
        s = "%s ~ %s" % (start.strftime("%Y-%m-%d %H:%M") ,end.strftime("%Y-%m-%d %H:%M"))

    return s
