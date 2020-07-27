from . import views
from django.urls import path


urlpatterns = [
    path('register/', views.register),    # 用户注册
    path('login/', views.login),    # 用户登录
    path('logout/', views.logout),    # 用户登录
]
