# 如果一个模块文件中有__all__变量，当使用from xxx import *导入时，只能导入这个==列表==中的元素。

__all__ = ['func1']

def func1():
    print('This is func1')

def func2():
    print('This is func2')