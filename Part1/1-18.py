# coding:utf-8
# 将名称映射到序列的元素中

# 通过名称来访问元素,以减少结构对于位置的依赖性
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['name', 'joinDate'])
# 此处namedtuple为一个工厂方法,传入元组的名称及对应位置上的名称
sub = Subscriber('a', '7/1/2017')
print(sub.name)
print(sub[0])
# 获得元组中的元素,可用名称或者下标

name, joinDate = sub
# 可进行元素分解

# sub.name='w' 直接通过名称为其赋值,无法进行
sub = sub._replace(name='w')
print('after_modify', sub)
# t通过_replace可对指定名称元素及逆行修改(创建了一个新的元组)

Subscriber2 = namedtuple('Subscriber2', ['name', 'number', 'price'])
info = Subscriber2('', 0, 0.0)
#预置一个默认的元组
def dict_to_info(s):
    return info._replace(**s)
#通过replace给元素进行赋值

a={'name':'w','number':'22','price':'10'}
print('a_value',*a)
result=dict_to_info(a)
print(result)

records = list()
records.append(sub)


def cost(records):
    total = 0.0
    for rec in records:
        total = total + rec[1] * rec[2]
    return total
# 进行计算时,若元素的对应位置发生改变,则需要进行改动,且使用位置表现力也不够

def cost2(records):
    total = 0.0
    for rec in records:
        # 如果records中的元素(类的实例)已经有了price和number属性,则不需要进行下面的显式操作
        s = Subscriber2(*rec)
        total = total + s.price * s.number
        # 直接通过名称调用
    return total
