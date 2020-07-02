"""
列表操作相关的小需求
"""
from functools import reduce


def list_distinct():
    """
    一般列表去重，且不改变原来顺序
    :return:
    """
    list_1 = [1, 4, 1, 9, 7, 4, 'aa', 'bb', 'aa']
    list_2 = sorted(set(list_1), key=list_1.index)
    print(list_2)
    return ''


def list_dict_distinct():
    """
    列表字典去重，不改变原本顺序,字典元素完全相同时认为重复
    :return:

    reduce() 函数会对参数序列中元素进行累积。
    函数将一个数据集合（链表，元组等）中的所有数据进行如下操作：
    用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
    得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
    """
    list_1 = [{'id': 1, 'name': '小李'}, {'id': 2, 'name': '小明'},
              {'id': 3, 'name': '小王'}, {'id': 1, 'name': '小李'}]
    list_2 = reduce(lambda x, y: x if y in x else x + [y], [[], ] + list_1)
    print(list_2)
    return ''


def list_dict_update():
    """
    列表字典中，对每个字典进行更新
    :return:
    """
    list_1 = [{'id': 1, 'name': '小李'}, {'id': 2, 'name': '小明'},
              {'id': 3, 'name': '小王'}, {'id': 1, 'name': '小李'}]
    [x.update(name='小哈哈') for x in list_1]
    print(list_1)
    return ''


def dict_append():
    """
    合并两个字典，解析字典,
    :return:
    """
    obj_1 = {"id": 1, "name": "王小明"}
    obj_2 = dict(**obj_1)
    print('字典不变：', obj_2)
    obj_3 = {"age": 18}
    obj_4 = dict(obj_1, **obj_3)
    print('字典合并：', obj_4)
    obj_5 = {"id": 2, "info": {"name": "李晓文", "age": 20}}
    obj_6 = dict(id=2, test=123, **obj_5.get('info'))
    print('字典解析：', obj_6)
    return ''


if __name__ == '__main__':
    pass
    # list_distinct()
    # list_dict_distinct()
    # list_dict_update()
    # dict_append()


