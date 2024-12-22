# 不定长元组参数, 我们可以通过*args对其进行接受, 其返回参数args是一个元组

def user_info(*args):
    print(args)
    print(type(args))

user_info('张三', 20, '深圳市')