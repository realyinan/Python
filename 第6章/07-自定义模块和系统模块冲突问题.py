import random

print(random.__file__)

# 引入某个模块 => 当前项目中寻找是否有同名的文件 => 如果找到则直接使用，未找到 => 继续向上寻找 => Python解析器中

print(random.randint(1, 10))