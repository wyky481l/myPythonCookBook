# coding:utf-8
# 筛选序列中的元素
mylist = [1, 4, -5, 3, 10, -7, 2, 3, -1]
list1 = [n for n in mylist if n > 0]
print(list1)
# 缺点,如果数据量超大,这样计算会在开始就产生一个庞大的结果。这里应该使用生成器

pos = [n for n in mylist if n > 0]
for i in pos:
    print(i)


# 使用生成器可解决上述问题
# 对于较为复杂的筛选标准,可使用filter()函数
def is_int(value):
    try:
        if value > 0:
            return True
    except ValueError:
        return False


list2 = list(filter(is_int, mylist))
print(list2)
# 可达到上面同样效果

list3 = [n * (-1) if n < 0 else n for n in mylist]
print(list3)
# 可对其中的元素进行筛选和转换/
from itertools import compress
charList = ['a', 'b', 'c', 'd', 'e', 'f']
counts = [1, 2, 3, 4, 5, 6]
boolList=[n%2==1 for n in counts]
#获得一个bool结果的list
result=list(compress(charList,boolList))
#compress接受一个待筛选序列以及一个布尔序列,自动将结果对应为true的值进行输出
#默认情况下,compress返回一个迭代器
print(result)
