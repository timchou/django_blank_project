# -*- coding: utf-8 -*-
import hashlib , os
import time,datetime,random,string,collections,httplib,urllib
from BeautifulSoup import BeautifulSoup
import xml.etree.ElementTree as ET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from djangoexample import opaque,consts
import json,urllib2,re,requests
from django.db import transaction
from django.conf import settings
from django.contrib.auth.models import User
from apps.users.models import UserProfile
from apps.articles.models import Article,WeiboUserRet
from apps.feeds.models import Feed
import collections
from readability.readability import Document
from weibo import APIClient,APIError
from django.db import IntegrityError
from lxml.etree import XMLSyntaxError
from djangoexample.settings import log_comm as logger

def myencode(s):
    '''
    将一个int转换成一个8位的字符
    '''
    encoder = opaque.OpaqueEncoder(consts.IDKEY)
    return encoder.encode_hex(s)

def mydecode(s):
    '''
    将一个8位的字符转换成一个int
    '''
    encoder = opaque.OpaqueEncoder(consts.IDKEY)
    return encoder.decode_hex( str(s) )

def generate_random_userv2(username,password):
    '''
    创建一个指定的的User
    '''
    newu = User.objects.create_user(username = username , password = password)
    newu.save()
    return newu
