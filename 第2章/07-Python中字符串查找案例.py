# 通过Python代码获取图片的后缀和代码
filename = input("请输入要上传的名称: ")
index= filename.rfind('.')

print(filename[:index])
print(filename[index+1:])
