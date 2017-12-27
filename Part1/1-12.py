# coding:utf-8
# 选出序列中出现次数最多的元素

from collections import Counter

words = ['a', 'a', 'a', 'b', 'b', 'c']
words2 = ['a', 'b', 'b']
word_count = Counter(words)

top_two = word_count.most_common(2)
print(top_two)
# [('a', 3), ('b', 2)] 输出对应元素及其出现的次数,Count实质上将元素和出现次数进行了映射

print(word_count['a'])
# 输出'a'的次数
word_count['b'] += 1
print(word_count)
word_count.update(words)
# 手动添加计数
print(word_count)

a = Counter(words)
b = Counter(words2)
c = a + b
d = a - b
print(c)
print(d)
#可进行简单的数学运算
