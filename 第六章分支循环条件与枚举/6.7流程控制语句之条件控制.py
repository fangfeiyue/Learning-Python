#coding=utf-8

''' a = 1
b = 2

if a > b :
    print('go to left');
else :
    print('go to right'); '''
    
''' 模拟用户登录
    1.判断用户输入的账号密码和存储的账号密码是否一致
        1.1一致，提示登录成功
        1.2不一致，提示账号或密码错误
            1.1账号或密码为空'''

account = 'ffy'
password = '123456'

print('请输入您的账号')
user_name = input()
print('请输入您的密码')
user_password = input()

if user_name and user_password :
    if user_name == account and user_password == password :
        print('load success');
    else :
        print('用户名或密码不正确');
else :
    print('用户名或密码不能为空');