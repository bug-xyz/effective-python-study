"""
加密解密相关
"""
import base64
import hashlib


def md5_encode(original_str, salt=''):
    """
    md5加密,md5加密是不可逆的，只能加密，不能解密，加密时只能传二进制类型的（字符串加encode()就能变成byte类型）。
    无论多长的字符串，加密出来都是32位的。
    提高安全性的方法：加盐。
    加盐是指在你输入的密码后面再加一个随机字符串。
    :param original_str:
    :param salt:
    :return:
    """
    m = hashlib.md5()
    new_str = original_str + salt
    m.update(new_str.encode(encoding='UTF-8'))
    print(m.hexdigest())
    return ''


def md5_file():
    """
    md5加密多用于判断文件是否有变化，版权问题，文件加水印之后，md5加密之后就不一样了
    :return:
    """
    f = open('common.py', 'rb')  # rb表示用二进制打开，
    jg = f.read()
    m = hashlib.md5(jg)  # 使用二进制打开，加密时不需要用encode
    result = m.hexdigest()  # 获取加密后的结果
    print(result)
    return ''


def base64_code():
    """
    base64 既能加密又能解密
    :return:
    """
    s = 'qwertyuiop'
    b = base64.b64encode(s.encode())  # 加密
    result = b.decode()
    print(result)
    b = base64.b64decode(result)  # 解密
    print(b.decode())


if __name__ == '__main__':
    pass
    # md5_encode('123456')
    # md5_file()
    # base64_code()





