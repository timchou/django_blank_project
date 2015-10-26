# -*- coding: utf-8 -*-
from rest_framework import serializers
from apps.users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    userid = serializers.SerializerMethodField()
    
    class Meta:
        model = UserProfile 
        fields = ( 'userid','nickname', 'introduce', 'weibo_id' ,'gender','weibo_ac_token','weibo_expires')

    def get_userid(self,obj):
        return obj.user.id
