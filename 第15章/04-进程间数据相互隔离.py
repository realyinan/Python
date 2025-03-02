import multiprocessing, time


# 进程之间数据相互隔离, 不能共享
# 子进程相当于父进程的副本, 即: 把父进程的内容会拷贝一遍, 单独执行. 注: main外的资源


my_list = []
print("看我执行了几次")

def write_data():
    for i in range(1, 6):
        my_list.append(i)
        print(f"add: {i}")
    
    print(f"write_data函数的结果: {my_list}")


def read_data():
    time.sleep(3)
    print(f"read_data函数的结果: {my_list}")



if __name__ == "__main__":
    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data)

    p1.start()
    p2.start()
