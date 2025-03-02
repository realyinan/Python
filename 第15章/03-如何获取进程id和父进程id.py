import multiprocessing
import time
import os

def coding(name, num):
    for i in range(num):
        print(f"{name}正在敲第{i}行代码")
        time.sleep(0.2)
        print(os.getpid(), multiprocessing.current_process().pid, os.getppid())

def music(name, count):
    for i in range(count):
        print(f"{name}正在听第{i}首音乐")
        time.sleep(0.2)
        print(os.getpid(), multiprocessing.current_process().pid, os.getppid())



if __name__ == "__main__":
    p1 = multiprocessing.Process(target=coding, name="A", args=("小明", 10))
    p2 = multiprocessing.Process(target=music, name="B", kwargs={"count": 10, "name": "小明"})

    print(p1.name)
    print(p2.name)

    p1.start()
    p2.start()

    # 打印main进程的pid
    print(os.getpid())

