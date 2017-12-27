# coding:utf-8
# 与字典有关的计算问题

student = {
    'a': 66,
    'b': 88,
    'c': 77,
    'd': 99,
}
min_stu = min(zip(student.values(), student.keys()))
# zip()将字典的key,value进行翻转
print(min_stu)

stu_sorted = sorted(zip(student.values(), student.keys()))
# 翻转后按照元素进行排序
print(stu_sorted)

info = zip(student.values(), student.keys())
min_info = min(info)
max_info = max(info)
# 这里将保存,因为zip()创建一个迭代器，其内容仅被消费一次，再次使用交会报错
print(min_info)
print(max_info)

