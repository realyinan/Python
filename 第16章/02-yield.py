def get_generator():
    for i in range(6):
        yield i

def my_generator():
    num = 0
    while True:
        yield num
        num += 1

res = get_generator()
res2 = my_generator()
print(res)
print(res2)
print("-"*20)

for i in res:
    print(i)