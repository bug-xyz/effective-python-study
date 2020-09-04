
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('user/', include('apps.user.urls')),   # 用户相关逻辑
    path('common/', include('apps.common.urls')),   # 通用
]

"""
@apiDefine  10  用户
"""
"""
@apiDefine  20  通用
"""