import threading, time

def coding(name, num):
    for i in range(num):
        print(f"{name}正在敲第{i}行代码")
        time.sleep(0.2)

def music(name, count):
    for i in range(count):
        print(f"{name}正在听第{i}首音乐")
        time.sleep(0.2)


if __name__ == "__main__":
    t1 = threading.Thread(target=coding, args=("小明", 10))
    t2 = threading.Thread(target=music, kwargs={"count": 10, "name": "小明"})

    print(t1.name)
    print(t2.name)

    t1.start()
    t2.start()
