
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    gender = models.IntegerField('性别', default=0)  # 0未设置，1男，2女
    name = models.CharField('真实姓名', max_length=64, default='')
    phone = models.CharField('手机号', max_length=11)
    status = models.IntegerField('用户状态', default=1)  # -1:删除 0:禁用 1:正常

    class Meta:
        db_table = 'user'



