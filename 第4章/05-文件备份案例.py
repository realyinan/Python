oldname = input("请输入文件名: ")
index = oldname.rfind('.')
name = oldname[:index]
postfix = oldname[index:]
newname = name + '备份'+ postfix

old_f = open(oldname, 'rb')
new_f = open(newname, 'wb')

while True:
    content = old_f.read(1024)
    if len(content) == 0:
        break
    new_f.write(content)

old_f.close()
new_f.close()
