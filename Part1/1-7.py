# coding:utf-8
# 让字典保持有序

from collections import OrderedDict

d=OrderedDict()
d['a']=1
d['b']=2
d['c']=3
for key in d:
    print(key,d[key])
#该dict的输出顺序，严格按照元素添加时的顺序
#OrderedDict内部维护一个双向链表,新加入的元素放置在链表的末尾,对已存在的键重新赋值不会影响其位置
#由于创建了链表，故其大小为普通dict的2倍
