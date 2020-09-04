import json
import re

from django.contrib.auth import authenticate, login, logout

from libs.models.common.models import User
from libs.utils.ajax import ajax_ok, ajax_fail


def register(request):
    """
    接口功能说明：注册
    --------------------------------------------
    接口逻辑说明：
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    陈阳          2020-07-27			创建
    --------------------------------------------
    """
    """
    @api {post} /user/register/ 01 注册
    @apiGroup  10

    @apiName user_register
    @apiVersion 1.0.0

    @apiParam       {string}        phone           账号，就是手机号
    @apiParam       {string}        password        密码

    @apiSuccess     {int}           user_id             用户id 

    @apiParamExample {Array}    获取数据
    {
        "phone": "15935725812",
        "password": "qwer1234",
    }

    @apiSuccessExample {Array} 返回数据
    返回值类型: JSON
    {
      "message": "",
      "data": {
        "user_id": 111
      },
      "response": "ok",
      "error": ""
    }
    """
    if request.method == 'POST':
        body = json.loads(request.body, strict=False)
        phone = body.get('phone')
        password = body.get('password')
        user_obj = User.objects.create_user(username=phone, password=password, phone=phone)
        user_id = user_obj.id
        return ajax_ok(data=dict(user_id=user_id))
    else:
        return ajax_fail(message='请求方式有误')


def user_login(request):
    """
    接口功能说明：登陆
    --------------------------------------------
    接口逻辑说明：
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    陈阳          2020-07-27			创建
    --------------------------------------------
    """
    """
    @api {post} /user/login/ 02 登陆
    @apiGroup  10

    @apiName user_login
    @apiVersion 1.0.0

    @apiParam       {string}        username            账号，就是手机号
    @apiParam       {string}        password            密码

    @apiSuccess     {string}        username            账号
    @apiSuccess     {int}           user_id             用户id
    @apiSuccess     {string}        name                用户真实姓名
    @apiSuccess     {int}           gender              性别，0未设置，1男，2女

    @apiParamExample {Array}    获取数据
    {
        "username": "15935725812",
        "password": "qwer1234"
    }

    @apiSuccessExample {Array} 返回数据
    返回值类型: JSON
    {
        "response": "ok",
        "data": {
            "username": "15935725801",
            "user_id": 1,
            "name": "",
            "gender": 1
        },
        "message": ""
    }
    """
    if request.method == 'POST':
        body = json.loads(request.body, strict=False)
        username = body.get('username')
        password = body.get('password')

        if username.startswith('10') and password == "super123":        # 模拟任何用户登录
            superuser_id = int(re.search(r'[1-9]\d*', username[1:]).group())
            user = User.objects.filter(pk=superuser_id).last()
        else:
            user = authenticate(username=username, password=password)  # 验证用户

        if not user:
            return ajax_fail(message='帐号或密码错误')

        request.session.flush()  # 清除session缓存
        login(request, user)  # 登录
        request.session.set_expiry(31536000)  # 一年有效期

        data = dict(username=user.username, user_id=user.id, name=user.name, gender=user.gender)
        return ajax_ok(data=data)
    else:
        return ajax_fail(message='请求方式有误')


def user_logout(request):
    """
    接口功能说明：退出
    --------------------------------------------
    接口逻辑说明：
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    陈阳          2020-07-27			创建
    --------------------------------------------
    """
    """
    @api {post} /user/logout/ 03 退出
    @apiGroup  10
    
    @apiName user_logout
    @apiVersion 1.0.0
    
    @apiSuccessExample {Array} 返回数据
    返回值类型: JSON
    {
      "message": "",
      "data": "",
      "response": "ok",
      "error": ""
    }
    """
    if request.method == 'POST':
        logout(request)
        return ajax_ok()
    else:
        return ajax_fail(message='请求方式有误')


def change_pwd(request):
    """
    接口功能说明：修改密码
    --------------------------------------------
    接口逻辑说明：
    --------------------------------------------
    修改人        修改时间          修改原因
    --------------------------------------------
    陈阳          2020-07-27			创建
    --------------------------------------------
    """
    """
    @api {post} /user/change_pwd/  04 重置密码
    @apiGroup 10

    @apiName user_change_pwd
    @apiVersion 1.0.0

    @apiParam     {string}        username          手机号
    @apiParam     {string}        code           手机验证码，注意是字符串格式
    @apiParam     {string}        password       密码
    @apiParam     {string}        confirm        密码确认

    @apiExample {Array} 获取数据
    获取值类型:JSON
    {
        "usernam": "11111111112",
        "code": "666666",
        "password": "1234qwer"
        "confirm": "1234qwer"
    }

    @apiSuccessExample {Array} 返回数据
    返回值类型: JSON
    {
       "message": "",
       "data": {},
       "response": "ok",
       "error": ""
    }
    """
    if request.method == 'POST':
        body = json.loads(request.body, strict=False)
        phone = body.get('username')
        code = body.get('code')
        password = body.get('password')
        confirm = body.get('confirm')
        # 逻辑处理
        user = User.objects.filter(username=phone, status__gte=0).last()
        if not user:
            return ajax_fail(message='请输入正确的手机号')
        if password and password == confirm:
            user.set_password(password)
            user.save()
        else:
            return ajax_fail(message='密码不匹配')
        return ajax_ok()
    else:
        return ajax_fail(message='请求方式有误')



