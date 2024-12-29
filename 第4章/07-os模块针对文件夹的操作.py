import os

# os.path.exists() 判断文件或文件夹是否存在
# os.mkdir(新文件夹名称)	创建一个指定名称的文件夹
# os.getcwd()	current work directory，获取当前目录名称
# os.chdir(切换后目录名称)	change directory，切换目录
# os.listdir(目标目录)	获取指定目录下的文件信息，返回列表
# os.rmdir(目标目录)	用于删除一个指定名称的"空"文件夹

os.chdir('./第4章')
print(os.getcwd())

print(os.listdir())