'''
    login
'''
ACCOUNT = 'ffy'
PASSWORD = '123456'

print'please input your account'
USER_NAME = raw_input()
print'please input your password'
USER_PASSWORD = raw_input()

if USER_NAME and USER_PASSWORD:
    if USER_NAME == ACCOUNT and USER_PASSWORD == PASSWORD:
        print'load success'     
    else:
        print'account or password is error'
else:
    print'account or passworld can not empty'
