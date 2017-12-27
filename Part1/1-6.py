# conding:utf-8
# 在字典中将键映射到多个值上
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
d.setdefault('a', []).append(3)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(3)
print(d)
# 选择不同的方式进行实现
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})
# defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {3}})

d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
# 手动创建时，对于第一个初始值，需要建立一个空的key-value
# 对于defaultdict则不需要
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
