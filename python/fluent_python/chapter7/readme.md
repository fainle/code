### 第七章 函数装饰器和闭包
#### 强大的功能，但是想要掌握，必须理解闭包


装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）

装饰器可能会处理被装饰函数，然后把它返回，或者替换为另外一个函数或调用对象。


register.ipynb 演示了装饰器的基础方法。

order.ipynb 演示了用装饰器模式重构的“策略”设计模式。

variable.ipynb 演示了全局变量和局部变量，以及python在局部里面对全局变量赋值的区别。

average_oo.ipynb 演示了闭包的普通使用。

times.ipynb 简单的装饰器用法。(记录函数的执行时间)

times2.ipynb 简单的装饰器用法。(对比上面增加了wraps复制被装饰函数的属性和参数)。

lru_cache.ipynb 缓存装饰器 lru_cache （参数必须可散列的）可以显著节省时间。

singledispatch.ipynb 模仿java的参数重载，用singledispatch装饰器实现。