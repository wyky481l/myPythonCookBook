# coding;utf-8
# 两个字典中寻找相同点

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'x': 4,
    'y': 2,
    'w': 5
}

info1 = a.keys() & b.keys()
print(info1)
# {'x','y'} 相当于取a与b的交集

info2 = a.keys() - b.keys()
print(info2)
# {'z'} 取a中存在,b中不存在的元素

info3 = a.items() & b.items()
print(info3)
# {('y', 2)} 取a和b中相同的项

#字典中的键由于其具有唯一性,正常的集合操作(并交差)均可使用,而value则无法进行
