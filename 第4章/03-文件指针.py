# offset：必需，表示相对于 whence 指定位置的偏移量（以字节为单位）。
# 正值：向文件尾方向移动。
# 负值：向文件头方向移动（仅在 whence=2 时允许）。
# whence：可选，表示参考点（默认值为 0）。
# 0：从文件的开头计算（默认）。
# 1：从当前位置计算。
# 2：从文件的结尾计算。


f = open('./第4章/python.txt', 'r', encoding='utf-8')

print(f.readlines())

f.seek(0)

for i in f.readlines():
    print(i)


