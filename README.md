# Pour l'etoile

右上角打包下载。下载到本地以后解压。

苹果电脑按Command+space搜Terminal打开终端。

在终端里切到文件夹位置，输"cd [路径]"  
__例__: 
``cd Document/Pour-l-etoile``



### 生成倒序版词库（按词尾排序）
输入
``python reverse.py`` 
词库会自动存入文件名为“Reversed.txt”的txt文件中。

### 生成乱序版词库
输入
``python shuffle.py``
或
``python shuffle.py [seed]``
可根据种子名生成固定的乱序词库。
词库会被自动存入文件名为“version_[seed].txt”的txt文件中。

__例__: 
``python shuffle.py abc``会生成文件“version_abc.txt”

### 查词
输入
``python search.py [word]``
可调出词条完整内容。

输入
``python search.py [word] -ant``
可调出该词条及其所有反义词词条。

输入
``python search.py [word] -syn``
可调出该词条及其所有近义词词条。

也可输入``python search.py [word] -syn -ant``。

__例__: 
``python search.py abandon -syn -ant``
