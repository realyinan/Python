i = 0
while i < 5:
    if i == 2:
        print("遇到2不打印")
        i += 1
        continue
    print(i)
    i += 1
print("="*8)

i = 0
while i < 5:
    if i == 2:
        print("遇到2退出")
        break
    print(i)
    i += 1