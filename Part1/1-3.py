# coding:utf-8
# 保存最后N个元素

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
            # 从此处返回,下次迭代再从此处继续
    previous_lines.append(line)


if __name__ == '__main__':
    with open('../bookCatalog.txt') as f:
        for line, prevlines in search(f, '1.2', 5):
            for pline in prevlines:
                print(line, end='')
            print(line, end='')

q = deque(maxlen=3)
# 设定队列的固定长度,满足先进先出原则
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
w = deque()
# 创建一个无界队列
w.appendleft(2)
w.popleft()
#可在两端执行添加弹出操作
