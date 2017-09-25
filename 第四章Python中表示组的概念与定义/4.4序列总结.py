#coding=utf-8

#str、list、tuple都是序列
print(3 in [1, 2, 3, 4]);#True
print(3 in (1, 2, 3, 4));#True
print(3 not in (1, 2, 3, 4));#False

#序列长度
print(len((1, 2, 3, 4, 5, 6)));#6
print(len([1, 2, 3, 4, 5, 6]));#6
print(len("[1, 2, 3, 4, 5, 6]"));#18

#序列中最大值
print(max([1, 2, 3, 4, 5, 6]));#6
print(min([1, 2, 3, 4, 5, 6]));#1
print(max("hello world"));#w

#输出对应字符的ascii码ord()
print(ord('w'));#119
print(ord('d'));#100

