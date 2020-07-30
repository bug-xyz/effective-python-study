# coding: utf-8
import logging
import time

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404
from django.utils.deprecation import MiddlewareMixin

from libs.utils.ajax import ajax_fail

log = logging.getLogger(__name__)

# 无需登录接口
no_login_urls = ['apidoc', 'register', 'login', 'change_pwd']


class AuthenticationMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        """
        功能说明：请求确定视图函数之前
        ----------------------------------------
        修改人     修改时间        修改原因
        ----------------------------------------
        陈阳      2020-07-30
        --------------------------------------------
        """
        re_method = request.method
        if re_method == 'OPTIONS' or (re_method == 'POST' and not request.body):    # post请求即便没有参数也要传{}
            return HttpResponse()

        # 权限验证
        if next((False for x in no_login_urls if x in request.path), True):
            if request.user.is_anonymous:
                return ajax_fail(message="not_login")
            if not request.user.status:
                return ajax_fail(message="帐号被禁用，请联系管理员")
        return None

    def process_response(self, request, response):
        """
        功能说明：视图执行后
        ----------------------------------------
        修改人     修改时间        修改原因
        ----------------------------------------
        陈阳      2020-07-30
        --------------------------------------------
        """
        try:
            ip = request.META.get('HTTP_ORIGIN')
            response["Access-Control-Allow-Origin"] = '*'
            response["Access-Control-Allow-Credentials"] = 'true'
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
            response["Access-Control-Max-Age"] = "1728000"
            response["Access-Control-Expose-Headers"] = 'Date'
            use_time = time.time() - request.start_time
            if use_time > 3:  # 操作3秒写入慢执行日志
                log.warning("slow_log: use_time=%s path:%s %s" % (use_time, request.method, request.path),
                            extra=dict(req=request))
            if settings.DEBUG:
                if not request.path.lstrip('/').startswith(settings.STATIC_URL.lstrip('/')):  # lstrip增加设置中url前少写/的容错
                    # print 'use_time: %s %s %s' % (use_time, request.method, request.path)
                    pass
        except Exception as e:
            print(e)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        功能说明：请求确定视图函数之后，执行视图之前
        ----------------------------------------
        修改人     修改时间        修改原因
        ----------------------------------------
        陈阳      2020-07-30
        --------------------------------------------
        """
        request.start_time = time.time()

    def process_exception(self, request, exception):
        """
        功能说明：视图函数异常处理
        ----------------------------------------
        修改人     修改时间        修改原因
        ----------------------------------------
        陈阳      2020-07-30
        --------------------------------------------
        """
        if request.path.lstrip('/').startswith(settings.STATIC_URL.lstrip('/')):
            # 静态文件不处理错误
            return None

        if isinstance(exception, (PermissionDenied, Http404)):
            raise exception

        log.exception("", extra=dict(req=request))

        return ajax_fail(message=u"未知系统错误")
