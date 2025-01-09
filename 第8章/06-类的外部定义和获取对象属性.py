class Cat(object):
    def eat(self):
        print("吃猫粮")

    def drink(self):
        print("喝牛奶")

# 对象属性既可以在类外面添加和获取，也能在类里面添加和获取。

cat1 = Cat()

# 添加属性
cat1.name = "喵喵"
cat1.color = "Yellow"

# 访问属性
print(cat1.name)
print(cat1.color)
