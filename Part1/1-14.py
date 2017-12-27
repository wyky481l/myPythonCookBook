# coding:utf-8
# 对不原生支持比较操作的对象排序
from operator import attrgetter


class User:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return 'User({})'.format(self.id)


users = [User(1002), User(1001), User(1003)]
info = sorted(users, key=lambda u: u.id)
print(info)

infos = sorted(users, key=attrgetter('id'))
print(infos)
#后者也能完成目标,且可同时提取多个字段,速度更快

info_min=min(users, key=attrgetter('id'))
#对于min/max同样适用