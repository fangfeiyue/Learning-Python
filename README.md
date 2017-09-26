# Learning-Python
Python并不是一门新兴的语言，诞生于上世纪90年代初，随着大数据与人工智能的流行，Python逐步的流行了起来。可用于爬虫、大数据、测试、Web、AI等。   

Python之禅

Simple is better than complex.
简洁胜于复杂。

Now is better than never.Although never is often better than right now.做也许好过不做，但不假思索就动手还不如不做。

## 第一章、Pyton入门导学

### 1.1Python的特性

1.Python是一门编程语言，它只是众多编程语言中的一种  

2.语法简洁、优雅、编写的程序容易阅读  

3.跨平台，可以运行在Windows、Linux、MacOS  

4.易于学习  

5.极为强大而丰富的标准库与第三方库，比如电子邮件，比如图形GUI界面  

6.Python是一个面向对象的语言

7.Python既有动态脚本的特性，又有面向对象的特性

### 1.2Python的缺点
1.相较于C、C++、Java，运行效率较慢，原因之一就是C、C++属于编译型语言， 在程序运行之前有个运行编译的过程，通常会把源代码编译成机器码这个机器码是很接近底层的，所以运行效率是很高的，Python、Javascript属于解释型语言，没有编译的过程，所以每次执行程序都会去解析源代码 

2.为什么会有编译型语言和解释型语言呢？运行效率和开发效率很多时候很难兼得。   
## 第二章、Python的环境安装
1.去官网下载需要版本的Python:[官网](https://www.python.org/)

2.直接下一步下一步安装就可以

3.安装完成后，找到IDLE打开，会显示一个Python提供的编写代码的界面

4.在这个界面输入print('hello world')然后回车，就看到IDLE输出了hello world

## 第三章、理解什么是写代码与Python的基本类型
### 3.1什么是代码，什么是写代码
1.什么是代码？代码是现实世界事物在j计算机世界中的映射

2.什么是写代码？写代码就是将现实世界中的事物用计算机语言来描述
### 3.2整型与浮点型
1.整数：int，Python里面没有shor、long类型

2.浮点数：float，Python的浮点类型没有单精度，双精度之分，Python的浮点型就是双精度的

3.type()可以查看数值是什么类型的
```
type(2/2);//float
type(2//2);//int
type(1);//int
``` 
### 3.3 十、二、八、十六进制
### 3.4 各进制的表示与转换
1.表示：
- Python中二进制的表示法必须加b：0b10

- Python中八进制的表示法必须加0：0o10

- Python中十六进制的表示法必须加x：0x10

- Python中八进制的表示法必须加0：0o10

2.转换
- 其他制转二进制用bin()
```
bin(10)//0b1010
bin(0o7)//0b111 
```
- 其他制转十进制用int()
```
int(0o77)//63
int(0b111)//7 
```
- 其他制转十六进制用hex()
```
hex(99)//0x63
hex(0o23)//0x13
```
### 3.5布尔类型与复数
1.bool类型
- True\False，首字母必须大写
```
bool(-1);//True
bool('1');//True
bool('');//False
bool(0);//False
bool([]);//False
bool({});//False
bool(None);/ /False
```
2.complex复数

- Python表示复数的方式，数字后面加j
```
36j
```

### 3.6字符串单引号、双引号
### 3.7多行字符串
- 使用三个引号（单、双引号都行）
```
'''
hello world
hello world
hello world
'''
```

### 3.8转义字符
### 3.9原始字符串
```
print(r'c:\norwind\west');//c:\norwind\west
print(r'let's');//语法错误
```
#### 3.10字符串的运算
- 中文注释要文件开头要加#coding=utf-8
- 单行注释#
- 多行注释'''内容'''
- 字符串拼接
```
print("hello"+"world"); 
print("hello"*3);# 输出三遍hellohellohello
``` 
- 获取单个字符串
```
print("hello world"[3]);#l 
print("hello world"[-1]);#d
```
- 截取指定的字符串[x-y]不包含y
```
print("hello world"[0:4]);
print("hello world"[0:-3]);#hello wo
print("hello world"[0:-1]);#hello worl

#输出world
print("hello world"[6:11]);
print("hello world"[6:]);

#截取最后的one
print("hello world hello people hello everyone"[-3:]);
```

## 第四章、Python中表示组的概念与定义
### 4.1列表的定义
```
print(["hello",1, 2, 3, 4, 5]);#可以输入多种类型
print([[1, 2, 3],['h', 'e', 'l']]);#嵌套列表
```
### 4.2列表的基本操作
- 访问列表中的某个元素
```
print(["新月打击", "苍白之爆", "月之降临", "月神冲刺"][0]);
print(["新月打击", "苍白之爆", "月之降临", "月神冲刺"][0:2]);#输出的还是一个列表：['新月打击', '苍白之爆']
print(["新月打击", "苍白之爆", "月之降临", "月神冲刺"][-1:]);#['月神冲刺']
```
- 合并两个列表用加号
```
print(["新月打击", "苍白之爆", "月之降临", "月神冲刺"]+["苍白纸人", "血色满天"]);
['新月打击', '苍白之爆', '月之降临', '月神冲刺', '苍白纸人', '血色满天']
```
- 不能使用减法操作符
```
print(["新月打击", "苍白之爆", "月之降临", "月神冲刺"]+["月之降临", "月神冲刺"]);#报错
```
- 追加元素
```
a = [1, 2, 3, 4];
a.append(34);
print(a);
```
### 4.3元组(tuple)
- 定义元组
```
print((1, 2, 3, 4, 5));
print(("hello", -2, 3, 4, True));
```
- 访问单个元素
```
print(("hello", -2, 3, 4, True)[1]);#=2
```

- 选取一个元组的范围
```
print(("hello", -2, 3, 4, True)[1:4]);#(-2, 3, 4)
```
- 元组相加,元素不能少于两个
```
print((1, 2, 3, 4,'23', True)+('sdf',4, 5, 6, 7, 'ss'));#(1, 2, 3, 4, '23', True, 'sdf', 4, 5, 6, 7, 'ss')

print((1)*3);#3
print([1]*3);#[1, 1, 1]
print(('ss')*3);#ssssss, str类型

#空元组
print(type(()));

#定义只有一个元素的元组
print(type((1,)));
```

### 4.4序列总结

- str、list、tuple都是序列
- 序号
```
[1, 2, 34, 4][1]
```
- 切片
```
[1, 2, 34, 4][1:2]
```
- +，*

- 判断某个元素是否包含在序列中
```
print(3 in [1, 2, 3, 4]);#True
print(3 in (1, 2, 3, 4));#True
print(3 not in (1, 2, 3, 4));#False
```

- 序列长度
```
print(len((1, 2, 3, 4, 5, 6)));#6
print(len([1, 2, 3, 4, 5, 6]));#6
print(len("[1, 2, 3, 4, 5, 6]"));#18
```

- 序列中最大值
```
print(max([1, 2, 3, 4, 5, 6]));#6
print(min([1, 2, 3, 4, 5, 6]));#1
print(max("hello world"));#w
```

- 输出对应字符的ascii码ord()
```
print(ord('w'));#119
print(ord('d'));#100
```
### 4.5set集合
1.集合的特点：
- 无序

- 元素不重复

2.支持的操作
- 获取长度
```
print(len({1,3, 4}))#3
```
- 是否包含某个元素
```
print(3 in {1,3, 4})#True
print(3 not in {1,3, 4})#False
```
- 求两个集合的差集
```
print({1, 2, 3, 4, 5, 6} - {2,3});#set([1, 4, 5, 6])
```
- 求两个集合的交集
```
print({1, 2, 3, 4, 5, 6} & {2,3});#set([2, 3])
```
- 求两个集合的并集
```
print({1, 2, 3, 4, 5, 6} | {2,3,10});#set([1, 2, 3, 4, 5, 6, 10])
```
- 定义一个空的集合
```
print(set());#set([])
```
- 删除某项
```
set1.remove(1);
```
- 添加一项
```
set1.add(10);
```
- 添加多项
```
set1.update(['a', 'b', 'c', 'd']);
```
### 4.6dict字典
- 键不能重复
- 键不一定非要是字符串，数值也行
- key必须是不可变的类型，如int，str
- 创建一个空的字典
```
print(type({}))
```
## 第五章、变量与运算符
### 5.1什么是变量
```
list = [1, 2, 3, 4];
print(list);
```
### 5.2变量命名规则
- 字母、数字、下划线，首字母不能是数字
- 不能用系统关键字
- 变量名区分大小写

### 5.3值类型与引用类型
1.值类型
- int
- str
- tuple

2.引用类型
- list
- set
- dic
3. id()用于显示某个变量在内存中的地址

### 5.4列表的可变与元组的不可变
```
a = (1, ['h', 'i', 'j', 'k']);
print(a[0]);# 1
#a[1] = 2; 报错，元组不可变
a[1][2] = 'm';
print(a);# 1, ['h', 'i', 'j', 'k']
```
### 5.5运算符号
- 整除：//
```
print(5//2);#2
```
- 余数：%
```
print(5%2);#1
```
- 幂运算
```
print(2**5);#2的五次方
```
### 5.6赋值运算符
1.分页加载总页数计算公式
```
totalPage = (totalCount+ loadCount-1) / loadCount;
其中 loadCount- 1 就是 totalCount/ loadCount的最大的余数
```

2.Python里面没有自增自减运算符
```
a = 1;
print(c++);#报错
print(c--);#报错
```

### 5.7关系运算符
### 5.8不只是数字才能做比较运算
### 5.9逻辑运算符
- and
- or
- not
### 5.10成员运算符
- 作用：判断一个元素是否在另外一组元素里面，成员运算符的返回值依然是bool类型
- in可以用在str,元组,列表,set集合,字典
```
字典中判断是key值是否存在
b = 'b';
print(b in {'b':b}); #True
```
- not in
### 5.11身份运算符
- is
- not is
- is 和 == 的区别, ==比较是值是否相等，is比较的是两个变量的身份是否相等。
```
a = 1.0;
b = 1;
print(a == b); #True
print(a is b); #False

#集合 集合是无序的
a1 = {1, 2, 3}
b1 = {2, 1, 3}
print(a1 == b1); #True
print(a1 is b1); #False 

#元组 元组是有序的
a = (1, 2, 3);
b = (3, 2, 1);
print(a == b); #False
print(a is b); #False

#列表
a = [1, 2, 3];
b = [3, 2, 1];
print(a == b); #False
print(a is b); #False

#字典
a = {"a":"b", "c":"d"};
b = {"c":"d", "a":"b"};
print(a == b); #True
print(a is b); #False
```
### 5.12如何判断变量的值，身份和类型 
- isinstance(var, type) 判断类型，为什么不用type()呢，因为type没法判断子类属于某种类型的
```
type可以写成一个元组
isinstance(a, (int, float, str));判断是不是元组中的任意一种类型
```
- is 身份
- == 值
### 5.13位运算符 都是把数字当做二进制数进行处理
- & 按位与
- | 按位或
- ^ 按位异或
- ~ 按位取反
- << 左移动
- 右移动>>

## 第六章、分支、循环、条件与枚举
### 6.1什么是表达式
### 6.2表达式的优先级
- and的优先级高于or
- 表达式优先级图标

![优先级](http://note.youdao.com/yws/public/resource/c2361265179a03449f6d52397fd50033/xmlnote/46197B50861A43948F0E3A1DDF8A8C9C/17814)
### 6.3表达式优先级练习
### 6.4在文本文件中编写Python代码
### 6.5熟悉vscode开发环境与Python插件安装
### 6.6流程控制语句之条件控制
### 6.7流程控制语句之条件控制
### 6.8常量与pylint的规范
### 6.9流程控制语句之条件控制 三 snippet、嵌套分支、代码块的概念
### 6.10流程控制语句之条件控制 四 elif的优点
### 6.11 思考题解答与改变定势思维                
