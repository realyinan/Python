# 1. 线程之间执行是无序的
# 2. 主线程会等待所有的子线程执行结束再结束
# 3. 线程之间共享全局变量
# 4. 线程之间共享全局变量数据出现错误问题


import time, threading


def print_info():
    time.sleep(0.5)
    th = threading.current_thread()
    print(f"当前正在执行的线程: {th}")


if __name__ == "__main__":
    for i in range(10):
        th = threading.Thread(target=print_info)
        th.start()