for i in "Beatles":
    if i == "t":
        print("终止打印")
        break
    print(i)
print('='*8)
for i in "Beatles":
    if i == "t":
        print("不打印t")
        continue
    print(i)