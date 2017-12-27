# coding:utf-8
# 将序列分解为单独的变量

p = (4, 5)
x, y = p
print(x, y)
# 对于可迭代的对象,可通过简单的赋值从而分解单独的变量
# 前提是,变量的数量和结构需要和序列一致

data = ['student1', 18, 'man', (1995, 7, 7)]
name, age, sex, birth = data
year,month,day=birth
print(birth,day)
#若序列中的元素仍然是可迭代的,则可继续分解

a,b,c=sex
print(a,b,c)
#字符串是可迭代的,所以逐个获得字母

_,age,sex,_=data
#有时需要获得中间特定的值,但获取时两侧的变量必须存在,所以选择一个用不到的变量作为丢弃的名称

