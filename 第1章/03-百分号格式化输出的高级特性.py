name = 'Paul'
age = 25
num = 12
weight = 45.6

print('name: %s, age: %d, number: %06d, weight: %.2f' % (name, age, num, weight))

# %s	字符串	"Hello %s" % "World"
# %d	十进制整数	"%d apples" % 5
# %f	浮点数	"%.2f" % 3.14159
# %x	十六进制整数	"%x" % 255
# %o	八进制整数	"%o" % 255
# %e	科学计数法	"%.2e" % 123456.789
# %%	字面百分号	"Discount: %d%%" % 50