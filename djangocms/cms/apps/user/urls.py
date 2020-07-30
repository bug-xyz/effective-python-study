from . import views
from django.urls import path


urlpatterns = [
    path('register/', views.register),    # 用户注册
    path('login/', views.user_login),    # 用户登录
    path('logout/', views.user_logout),    # 用户登录
    path('change_pwd/', views.change_pwd),    # 修改密码
]
