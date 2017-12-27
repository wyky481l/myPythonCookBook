# coding:utf-8
# 同时对数据做转换和换算

nums=[1,2,3,4,5]
s=sum(x*x for x in nums)
#min/max等计算亦可
print(s)
#上面是在参数中使用生成器

s2=sum([x*x for x in nums])
print(s2)
#这是正常的写法,将生成的结果放入元组中,再进行计算
#但多引入额外的列表,数据量较大时,耗费资源较多.故基于生成器则更优