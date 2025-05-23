def check(fn):
    def inner():
        print("请登录")
        fn()
    return inner


def comment():
    print("发表评论")


comment = check(comment)
comment()


# 在不改变现有函数源代码以及函数调用方式的前提下，实现给函数增加额外的功能。
# 装饰器的本质就是一个闭包函数（三步：① 有嵌套 ② 有引用 ③ 有返回和额外功能）
# 函数名作为实参传递，本质上传递的是对应函数的地址。
# 内部函数的形式必须和原函数要保持一致 即: 要有参数都有参数, 要有返回值否有返回值