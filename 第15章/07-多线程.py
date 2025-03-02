# 进程是分配资源的基本单位, 一旦创建一个进程就会分配一定的资源.
# 线程是cpu调度的基本单位，每个进程至少都有一个线程，而这个线程就是我们通常说的主线程。

import threading, time


def coding():
    for i in range(10):
        print(f"敲代码.....{i}")
        time.sleep(0.2)

def music():
    for i in range(10):
        print(f"听音乐.....{i}")
        time.sleep(0.2)



if __name__ == "__main__":
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)

    t1.start()
    t2.start()
