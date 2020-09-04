from . import views
from django.urls import path


urlpatterns = [
    path('geturlzip/', views.get_url_zip),  # 获取图片并压缩
]
