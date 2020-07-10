"""
字典操作相关的小需求
"""


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


class Ddict(dict):
    """
    - 为字典加上点语法. 例如:
    # >>> o = Ddict({'a':1})
    # >>> o.a
    # >>> 1
    # >>> o.b
    # >>> None
    """

    def __init__(self, dictobj={}):
        self.update(dictobj)

    def __getattr__(self, name):
        # Pickle is trying to get state from your object, and dict doesn't implement it.
        # Your __getattr__ is being called with "__getstate__" to find that magic method,
        # and returning None instead of raising AttributeError as it should.
        if name.startswith('__'):
            raise AttributeError
        return self.get(name)

    def __setattr__(self, name, val):
        self[name] = val

    def __hash__(self):
        return id(self)


def dict_reverse():
    """
    字典键值互换，利用推导机制（列表推导式）
    :return:
    """
    chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
    rank_dict = {y: x for x, y in chile_ranks.items()}
    print(rank_dict)
    chile_len_set = {len(x) for x in rank_dict.values()}  # 集合也可以利用推导机制
    print(chile_len_set)
    return ''


def little_knowledge():
    """
    小知识点
    :return:
    """
    a = {}
    b = a.setdefault(1, [])  # 不存在键时增加键值对，后续更新返回值会同步更新字典
    print(a, b)  # {1: []} []
    b.append(123)
    print(a, b)  # {1: [123]} [123]
    c = a.setdefault(1, None)  # 存在键时直接获取, 后续更新返回值会同步更新字典, 代码等效与 c = a.setdefault(1)
    c.append(456)
    print(a, c)  # {1: [123, 456]} [123, 456]
    return ''


if __name__ == '__main__':
    pass
    little_knowledge()
    # dict_append()
    # aa = Ddict()
    # aa.bb = 'bb'
    # aa.cc = 'cc'
    # print(aa, aa.bb, aa.cc)
    # dict_reverse()


