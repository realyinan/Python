import time as t

start = t.time()

list1 = []
for i in range(100000):
    list1.append(i)

end = t.time()

print(f"{end - start:.5f}")