# 多任务是指在同一时间内执行多个任务
# 多任务的两种表现形式
# 并发：在一段时间内，交替执行任务
# 并行：在一段时间内，真正的同时一起执行多个任务
# 进程（Process）是CPU资源分配的最小单位，它是操作系统进行资源分配和调度运行的基本单位

import multiprocessing
import time

def coding():
    for i in range(10):
        print(f"敲代码.....{i}")
        time.sleep(0.2)

def music():
    for i in range(10):
        print(f"听音乐.....{i}")
        time.sleep(0.2)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)

    for i in range(10):
        print(f"main.....{i}")
        time.sleep(0.2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("主进程执行完毕")


   