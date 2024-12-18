person = {'name':'孙悟空', 'age': 600, 'address':'花果山'}
print(person['name'])

# get(key, 默认值) 根据字典的key获取对应的value值，如果当前查找的key不存在则返回第二个参数(默认值)，如果省略第二个参数，则返回None
print(person.get('name', '猪八戒'))
print(person.get('job'))
print(person.get('job', '保镖'))

print(person.keys())
print(person.values())
print(person.items())
for i, j in enumerate(person.items(), 1):
    print(i, j)