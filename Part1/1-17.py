# coding:utf-8
# 从字典中提取子集

price = {
    'a': 45,
    'b': 600,
    'c': 205,
    'd': 10
}

p1={key:value for key,value in price.items() if value>200}
print(p1)

names={'b','d'}
p2={key:value for key,value in price.items() if value>200 and key in names}
print(p2)
#上述方式使用的是字典推导式

p3=dict((key,value) for key,value in price.items() if value>200)
print(p3)
#通过创建元组序列，再使用dict()

p4={key:price[key] for key in price.keys() if price[key]>200}
print(p4)
#下面两种方式均可以达到目标，但实际运行时耗费时间较多
