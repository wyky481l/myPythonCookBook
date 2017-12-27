# conding:utf-8
# 实现优先级队列
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-property, self._index, item))
        #其实质为按照对应项进行由小到大排序,若遇到相同项则依据后面一项进行。对象不可进行排序,强制进行则会报错
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
        #返回最后一项,即item

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
