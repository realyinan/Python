# 进程之间数据是相互隔离的, 同一个继承中的线程数据是可以共享的

import threading, time

my_list = []

def write_data():
    for i in range(50):
        my_list.append(i)
        print(f"add {i}")
    print(f"write_data函数: {my_list}")

def read_data():
    time.sleep(3)
    print(f"read_data函数 :{my_list}")


if __name__ == "__main__":
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)

    t1.start()
    t2.start()