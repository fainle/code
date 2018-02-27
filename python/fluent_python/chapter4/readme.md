### 第四章 文本和字节序列
#### 人类使用文本，计算机使用字节序列

Unicode 有非常明确的定义。(python3.4 以后使用的标准是 Unicode 6.3)
其中4-6个16进制表示码位。(并且有前缀 U+) 例如：字母A(U+0041) 10%的有效码位有对应的字符。
字符的编码取决于采用的什么算法。utf-8编码 A 是 \x41 而 utf-16 是 \x41\x00

utf8.ipynb 演示了utf-8编码与解码。

bytes_and_bytearray.ipynb 演示了简单的bytes 和 bytearray的用法。

struct.ipynb 使用struct模块来处理字节序列对象，包括二进制图片对象，这里演示用图片二进制的头部数据提取图片的长宽。

unicode_encode_error.ipynb 字符编码的常规错误处理方法。