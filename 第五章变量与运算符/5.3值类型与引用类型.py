#coding=utf-8
#值类型
"""a = 1;
b = 1;
a = 2;
print(a);#2
print(b);#1
"""

"""str1 = '123';
str2 = str1;
str1 = "3434";
print(str1);
print(str2);"""

"""tuple1 = (1, 2, 3, 4);
tuple2 = tuple1;
tuple1 = (4, 5, 6, 23);
print(tuple1);
print(tuple2);"""

#引用类型
"""list1 = [1, 2, 3, 4];
list2 = list1;
list1[0] = 'sd';
print(list1);
print(list2);"""

set1 = {1, 2, 3, 4, 5};
set2 = set1;
# 删除某项
set1.remove(1);
# 添加一项
set1.add(10);
# 添加多项
set1.update(['a', 'b', 'c', 'd']);
print(set1);
print(set2);

"""dic1 = {1:2};
dic2 = dic1;
dic1[0]="哈哈";
print(dic1);
print(dic2);"""