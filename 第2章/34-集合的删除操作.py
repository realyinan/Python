# remove()方法：删除集合中的指定数据，如果数据不存在则报错。
products = {'萝卜', '白菜', '水蜜桃', '奥利奥', '西红柿', '凤梨'}
products.remove('白菜')
print(products)
# products.remove('香蕉')


# discard()方法：删除集合中的指定数据，如果数据不存在也不会报错。
products.discard('西红柿')
print(products)
products.discard('香蕉')
print(products)


# pop()方法：随机删除集合中的某个数据，并返回这个数据。
products.pop()
print(products)
