# coding:utf-8
# 从序列中移除重复项且保持元素间的顺序不变

def deduqe(items):
    seen = set()

    for item in items:
        if item not in seen: 
            yield item
            seen.add(item)

a = [1, 2, 2, 3, 3, 4, 5, 6, 6]
print(list(deduqe(a)))
# 此处deduqe()为一个生成器,yield item相当于不断的往该list中添加元素

b=set(a)
#简单的方法可以使用,但无法保证元素的顺序不变





