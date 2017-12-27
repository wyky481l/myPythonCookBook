# coding:utf-8
# 将多个映射合并为单个映射
from collections import ChainMap

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}

c = ChainMap(a, b)
# 将a和b进行合并,若存在相同的元素，则采用第一个映射的值
# 其实质是简单的维护一个记录映射关系的列表,映射中的元素不会进行合并
print(c)  # ChainMap({'y': 2, 'x': 1}, {'y': 3, 'z': 4})
print(c['y'])  # 2

del c['y']
print(c['y'])  # 3
# 修改操作只会响应在第一个映射结构上

values = ChainMap()
values['x'] = 1
values = values.new_child({'x': 2})
# 两种添加新映射的方式
values['x'] = 3
# 若该映射不存在则创建,否则进行修改
print(values)  # ChainMap({'x': 2}, {'x': 1})

values = values.parents
print(values)  # ChainMap({'x': 1})
values = values.parents
print(values)  # ChainMap({})

# 从中取出最后一条映射

merged = dict(a)
merged.update(b)
# 使用update将两个字典进行合并,并返回一个新的字典
#需要构建一个完整的字典对象,对原始的字典进行修改不会反映到后面合并的字典上
#而使用chainMap则可以在原数据修改后，自动更新

