# coding:utf-8
# 通过公共键对字典列表排序
from operator import itemgetter

infos = [
    {'name': 'a', 'age': 20, 'uid': 1001},
    {'name': 'c', 'age': 19, 'uid': 1003},
    {'name': 'd', 'age': 23, 'uid': 1002},
    {'name': 'e', 'age': 20, 'uid': 1004}
]

row_by_age = sorted(infos, key=itemgetter('age'))
print(row_by_age)

row_by_uid = sorted(infos, key=itemgetter('uid'))
print(row_by_uid)

row_by_uid_age = sorted(infos, key=itemgetter('age', 'uid'))
print(row_by_uid_age)
# 以上为使用itemgetter进行单列或多列排序

row = sorted(infos, key=lambda r: (r['age'], r['uid']))
# 使用lambda也可完成同样效果,但实际中前种方法运行较快
