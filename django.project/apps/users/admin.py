# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from apps.users.models import *

class UserProfileInline(admin.StackedInline):
    fk_name = 'user'
    model = UserProfile
    can_delete = False

class UserAdmin(UserAdmin):
    def nickname(self, obj):
        return obj.userprofile.nickname

    list_display = ('id','username' , 'nickname', 'is_staff' )
    inlines = (UserProfileInline, )
    fieldsets = (
        (None,{'fields':('username','password','is_staff','is_superuser')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2','is_staff','is_superuser'),}),
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
