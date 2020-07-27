
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('user/', include('apps.user.urls')),   # 用户相关逻辑
]

"""
@apiDefine  10  用户
"""