# 多个装饰器的装饰过程是: 离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰，由内到外的装饰过程
# 装饰器从上到下执行

def check_user(fn):
    def inner():
        print("登录中")
        fn()
    return inner

def check_code(fn):
    def inner():
        print("校验验证码")
        fn()
    return inner

# comment() -> check_code() -> check_user()
# cc = check_code(comment)
# comment = check_user(cc)

@check_user
@check_code
def comment():
    print("发表评论")



comment()

