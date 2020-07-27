# coding=utf-8
import json

from django.http import HttpResponse


def ajax_ok(data='', message=''):
    """
    return a success response
    """
    return ajax_data(response='ok', data=data, message=message)


def ajax_fail(message='', data=''):
    """
    return an error response
    """
    return ajax_data(response='fail', data=data, message=message)


def ajax_data(response, data=None, message=''):
    """
    if the response_code is true, then the data is set in 'data',
    if the response_code is false, then the data is set in 'error'
    """
    json_data = json.dumps(dict(response=response, data=data, message=message))
    return HttpResponse(json_data)
