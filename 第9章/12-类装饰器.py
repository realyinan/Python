class Check():
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        print("请先登录")
        result = self.__fn(*args, **kwargs)
        return result

    
@Check
def comment(*args, **kwargs):
    print("发表评论")

# comment = Check()
# comment(*args, **kwargs)

# __call__() 方法是 Python 中的一个特殊方法（魔法方法），用于使对象像函数一样可调用。也就是说，如果一个类实现了 __call__() 方法，那么其实例可以像普通函数一样使用。

comment()