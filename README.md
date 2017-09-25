# Learning-Python
Python并不是一门新兴的语言，诞生于上世纪90年代初，随着da数据与人工智能的流行，Python逐步的流行了起来。可用于爬虫、大数据、测试、Web、AI等。   

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
