from libs.utils.ajax import ajax_ok


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
    @apiParam       {string}        code            六位数字验证码,注意是字符串

    @apiSuccess     {int}           user_id             用户id 

    @apiParamExample {Array}    获取数据
    {
        "phone": "15935725812",
        "password": "qwer1234",
        "code": "666666"
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
    return ajax_ok()


def login(request):
    return ajax_ok()


def logout(request):
    return ajax_ok()




