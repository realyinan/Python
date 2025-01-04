def add_num(a, b):
    return a + b

def sub_num(a, b):
    return a - b

print(__name__)

if __name__ == '__main__':
    print(add_num(10, 20))


# 引入一个魔术变量：__name__，其保存的内容就是一个==字符串类型==的数据。

# ==随着运行页面的不同，其返回结果也是不同的：==

# ① 如果__name__是在当前页面运行时，其返回结果为__main__

# ② 如果__name__在第三方页面导入运行时，其返回结果为模块名称（文件名称）


# ① 要求我们可以直接在模块文件中对代码进行直接测试

# ② 代码测试完毕后，当导入到其他文件时，测试代码要自动失效