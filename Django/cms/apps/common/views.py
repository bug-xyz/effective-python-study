import zipfile

import requests
from django.http import HttpResponse
from django.utils.encoding import escape_uri_path


def get_url_zip(request):
    """
    根据url加载图片，合并压缩，返回zip文件
    :param request:
    :return:
    """
    # 图片url列表
    urls = ['https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=639097614,3586063136&fm=26&gp=0.jpg',
            'https://b-ssl.duitang.com/uploads/blog/201403/20/20140320222843_MnP2A.jpeg',
            'https://b-ssl.duitang.com/uploads/item/201605/28/20160528212429_c2HAm.jpeg']
    # 新建响应，声明类型
    response = HttpResponse(content_type='application/zip')
    # 新建zip文件缓存
    z = zipfile.ZipFile(response, 'w', zipfile.ZIP_DEFLATED)
    # 遍历urls获取下标和值
    for i, url in enumerate(urls):
        # 请求图片url
        content = requests.get(url)
        # 将图片二进制写入zip文件中
        z.writestr('图片/%s.%s' % (i+1, url.split('.')[-1]), content.content)
    # 声明响应zip名称
    zip_name = '123中文.zip'
    # response['Content-Disposition'] = 'attachment; filename={}'.format(zip_name)  # zip_name无法显示中文
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(zip_name))   # 可以显示中文
    # return HttpResponse('==压缩成功==')
    return response

