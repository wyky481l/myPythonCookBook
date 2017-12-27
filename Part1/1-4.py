# coding:utf-8
# 找到最大或最小的N个元素
import heapq

nums = [1, 8, 2, 6, 3, 20, 18, 23, 4]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
# 输出最大,最小的三个数
print(sorted(nums)[-3:])
# 获取最大的三个

info = [{'name': 'apple', 'price': 10},
        {'name': 'orange', 'price': 8},
        {'name': 'banana', 'price': 9},
        {'name': 'pear', 'price': 11}]
cheap = heapq.nsmallest(2, info, key=lambda s: s['name'])
# 按照name的字母顺序进行排序
cheap2 = heapq.nsmallest(2, info, key=lambda s: s['price'])
# 按照price的数字顺序进行排序
print(cheap)
print(cheap2)

# 当要寻找的元素个数,相对于集合长度很小时,建议使用nlargest/nsmallest
# 当仅仅需要找到集合的最大或最小的元素,则建议使用max/min
# 当需要找的元素个数与集合长度相近时,应先对集合进行排序,再进行切片 sorted(items)[:N]/sorted(items)[:-N]
