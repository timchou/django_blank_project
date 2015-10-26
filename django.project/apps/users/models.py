# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User,Group

class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True)

    avatar   = models.CharField(max_length=255,blank=True,null=True,help_text=u"头像,url链接")
    gender   = models.IntegerField(default=0,help_text=u"性别,0保密；1男；2女")

    nickname = models.CharField(max_length=255,blank=True,null=True,help_text=u"昵称")
    email    = models.CharField(max_length=255,blank=True,null=True,help_text=u"邮箱")
    phone    = models.CharField(max_length=255,blank=True,null=True,help_text=u"手机")

    birth    = models.DateTimeField(blank=True,null=True,help_text=u"生日日期")
    country  = models.CharField(max_length=255,blank=True,null=True,help_text=u"国家")
    province = models.CharField(max_length=255,blank=True,null=True,help_text=u"省")
    city     = models.CharField(max_length=255,blank=True,null=True,help_text=u"市")
    addr     = models.CharField(max_length=255,blank=True,null=True,help_text=u"具体地址")
    introduce = models.TextField(blank=True,null=True,help_text=u"个人介绍")

    weibo_id = models.CharField(max_length=255,blank=True,null=True,help_text=u"微博uid")
    weibo_ac_token = models.CharField(max_length=255,blank=True,null=True,help_text=u"微博access token")
    weibo_expires  = models.CharField(max_length=255,blank=True,null=True,help_text=u"微博access token")
    weibo_since_id = models.CharField(max_length=255,blank=True,null=True,help_text=u"最后刷新的微博id")
    is_weibo_expires = models.IntegerField(default=0,help_text=u"微博token是否过期，0没有 1过期了")

    wx_openid = models.CharField(max_length=255,blank=True,null=True,help_text=u"微信openid")
    wx_unionid= models.CharField(max_length=255,blank=True,null=True,help_text=u"微信unionid")
    wx_expires  = models.DateTimeField(blank=True,null=True,help_text=u"微信access token过期日期")
    wx_ref_token = models.CharField(max_length=255,blank=True,null=True)
    wx_ac_token  = models.CharField(max_length=255,blank=True,null=True)

    gmt_created =   models.DateTimeField(auto_now_add=True)
    gmt_modify  =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"%d - %s" % ( self.user.id , self.nickname)

    def __unicode__(self):
        return u"%d - %s" % ( self.user.id , self.nickname)
