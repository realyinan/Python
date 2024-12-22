# 不定长字典参数, 我们可以通过**kwargs对其进行接受, 其返回参数kwargs是一个元组

def user_info(**kwargs):
    print(kwargs)
    print(type(kwargs))

user_info(name='张三', age=20, address='深圳市')