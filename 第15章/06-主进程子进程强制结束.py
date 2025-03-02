import time, multiprocessing

# 方式1: 设置子进程未守护进程, 当非守护进程结束时, 它的守护进程也会同步结束
# 方式2: 强制销毁子进程, 子进程会变为僵尸进程, 即: 资源不会被释放, 而是交由init进程来管理, 在合适的时机释放

def work():
    for i in range(10):
        print(f"第{i}天上班")
        time.sleep(0.2)



if __name__ == "__main__":
    p1 = multiprocessing.Process(target=work)
    # p1.daemon = True
    p1.start()
    time.sleep(1)
    p1.terminate()  # 强制销毁子进程, 会变为僵尸进程
    print("主进程结束")