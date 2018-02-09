### 第三章 字典与集合

python对字典和集合做了高度优化，字典是基于（散列表（hashtable））

可散列类型：在python里 如果一个值是可散列的，那么它在生命周期里值不可变。并且要实现`__hash__()`方法。所以列表不能作为字典的key,但是元祖（其中值全是可散列）可以。

create_dict.ipynb 展示了几种基本的数组创建方式。

str_key_dict.ipynb 实现了`__miss__`魔术方法，用于处理字典不存在的key的特殊情况。

ordered_dict.ipynb 实现了一个有序的字典。（内部感觉是用的元祖）

chain_map.py 是python3 才有的ChainMap类型，这种类型可以扫描每一个字典去匹配需要的key。在某种匹配的情况下很实用

user_dict.ipynb 是用python的userdict 实现的一个dict模拟。

mapping_proxy_type.ipynb 是MappingProxyType的一个例子，这个扩展类型的作用是实现了一个不可变的字典类型。不可变字典很多时候可以当配置使用。

list_set.ipynb 这里使用了set这个函数实现了一个去重的集合。也包括了2个集合 求差集（-） 合集（|） 和 并级（&）

