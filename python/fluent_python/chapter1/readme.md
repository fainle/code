### 第一章 主要是讲python的数据模型。

python 提供高度一致性的数据模型。

数据模型包括对python的描述，规范了语言自身的结构。（序列，迭代器，函数，类和上下文管理器）。

特殊方法能让自己更方便的使用python的(迭代，集合类，属性访问，运算符重载，函数和方法的调用，对象的创建和销毁，字符串格式化和上下文管理)

index0.py 展示了 `__getitem__` 和 `__len__` 特殊方法的用法，用纸牌来演示。也使用了
collections 的 部分内置数据结构。其中len(到类) 可以直接使用内置的ob_size数据结构，速度更快。

index1.py 展示了操作符重复载的方法 `__add__`, `__abs__`, `__repr__`, `__mul__`, `__bool__`, `__init__` 来实现了一个向量类。`__repr__`与`__str__`的区别在于，后者仅仅str或者print的时候才会被使用，如果`__str__`没被实现，则会使用`__repr__`。

`len`不是普通方法.而是使用了内置模型的方法。
