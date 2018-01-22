# -*- coding: utf-8 -*-
# 各种列表的操作时间负责度。
# 索引与分配 O(1)
# append O(1)
# + 这种链接符号 O(k) 
from timeit import Timer

def test1():
    l = []
    for i in range(10000000000):
        l = l + [i]
    return l
        
def test2():
    l = []
    for i in range(1000):
        l += [i]
    
def test3():
    l = []
    for i in range(1000):
        l.append(i)
        
def test4():
    l = [i for i in range(1000)]
    
def test5():
    l = list(range(1000))
    
t1 = Timer("test1", 'from __main__ import test1')
print("+:", t1.timeit(number  = 10000), '毫秒')

t2 = Timer("test2", 'from __main__ import test2')
print("+:", t2.timeit(number  = 10000), '毫秒')

t3 = Timer("test3", 'from __main__ import test3')
print("append:", t3.timeit(number  = 10000), '毫秒')

t4 = Timer("test4", 'from __main__ import test4')
print("推导式:", t4.timeit(number  = 10000), '毫秒')

t5 = Timer("test5", 'from __main__ import test5')
print("list range:", t5.timeit(number  = 10000), '毫秒')