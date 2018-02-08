### 第一章 序列构成的数组

容器序列：可支持不同的类型混合。（list, tuple, collections.deque），存的是值的引用。

扁平序列：仅支持一种数据类型。（str, bytes, bytearray, memoryview,  和 array.array），存的是值而不是引用。

可变序列：可变。 (list，bytearray，memoryview, array.array, collections.deque)

不可变序列：不可变。 (tuple, str 和 bytes)

可变支持方法 insert append reverse extend pop remove 方法(特殊方法 `__setitem__`, `__delitem__`, `__iadd__`)并且支持所有的不可变的方法。

不可变支持方法 index count 特殊方法(`__getitem__`, `__contains__`, `__iter__`, `__reversed__`)

所有的序列均支持 for * in 



listcomps.ipynb 实现了简单的列表推导式的写法.

listcomps2.ipynb 测试了内置的list推导与自定义函数的速度。

python2 有推导式的变量泄露问题。但是 python3 已经修复

list_sort.ipynb 里面有对比 sorted 和 *.sort 的区别 

bisect.ipynb 展示了 bisect 在有序列表里面做快速搜索的一些用处。非常实用

array.ipynb 展示了数组的基本用法，数组在存单一数据结构的时候，速度会比列表快很多。比普通文件读取速度快 70倍 写快7倍 且更省空间。（python 3.4 开始 数组类型不在支持 sort()）

pickle.ipynb pickle 是另外一种序列化的方案，速度和array相差无几，但是功能更强大，可以序列自定义类。





