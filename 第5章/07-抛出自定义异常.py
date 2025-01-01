# 在Python中，抛出自定义异常的语法为raise 异常类对象。

def input_password():
        password = input('请输入密码：')
        if len(password) < 6:
            raise Exception('密码长度不能小于6位')
        return


input_password()
                   