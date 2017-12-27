# conding:utf-8
# 根据字段将记录分组

from operator import itemgetter
from itertools import groupby

rows = [
    {'name': 'stu1', 'date': '07/02/2017'},
    {'name': 'stu2', 'date': '07/02/2017'},
    {'name': 'stu3', 'date': '07/01/2017'},
    {'name': 'stu4', 'date': '07/03/2017'},
    {'name': 'stu5', 'date': '07/04/2017'},
    {'name': 'stu6', 'date': '07/05/2017'}
]

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    # 类似于mysql中的group，将同样date的元素放在一起
    print(date)
    for i in items:
        print(i)

# 注意,这里使用groupby前,需要将数据进行排序,否则将无法获得对应的效果

from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

print(rows_by_date)
#这里将元素按照日期进行分类,但是无序的
