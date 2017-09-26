#condig=utf-8
"""a = [1, 2, 3];
print(hex(id(a)));

a.append(4);
print(a);
print(hex(id(a)));"""

"""a = [1, 2, 3, 4];
a.append(34);
print(a);"""

a = (1, ['h', 'i', 'j', 'k']);
print(a[0]);# 1
#a[1] = 2; 报错，元组不可变
a[1][2] = 'm';
print(a);# 1, ['h', 'i', 'j', 'k']