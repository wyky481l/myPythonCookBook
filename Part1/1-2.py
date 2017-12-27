# coding:utf-8
# 从任意长度的可迭代对象中分解元素

record = ('student', '14713044', 77, 88, 99)
name, sno, *score = record
# 这里使用*score将后面的元素全部包括
print(score)
score_avg = sum(score) / len(score)

*info, math_score = record
# 除最后一个元素以外,其他的全部包含在info中

records = [
    ('student1', 77),
    ('student2', 77, 88),
    ('student3', 77, 88, 99)
]
for name, *score in records:
    print(name, score)


# 对于变长的元组序列,可使用该方法获得元素

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
# 使用该方法可完成递归算法
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(items))
