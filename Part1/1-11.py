# coding:utf-8
# 对切片命名

items = [0, 1, 2, 3, 4, 5, 6, 7]
a = slice(2, 4)
# 在相应位置形成切面，并为其命名
print(items[a])

items[a] = [10, 11]
print(items)

del items[a]
# 对切片进行使用

s = 'helloworld'
print(a.indices(len(s)))
# (2,4,1) -->(start,stop,step)09
for i in range(*a.indices(len(s))):
    print(s[i])

# indices(size)将切片映射到特定大小的序列上,所有的值恰当地限制在边界内,防止了数组越界
