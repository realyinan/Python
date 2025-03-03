# 多线程并发操作统一数据, 有可能引发安全问题, 需要用到线程同步来解决
# 一个线程还没有完整的执行完之前, 被另一个线程抢走了资源, 就会出现非法值
# 在 Python 的 threading 模块中，join() 是一个线程对象（Thread 类实例）的方法，它的作用是阻塞调用它的线程，直到目标线程完成执行。简单来说，它让程序“等待”某个线程结束后再继续执行后续代码。

import threading, time
global_num = 0

def get_sum1():
    global global_num
    for i in range(10000000):
        global_num += 1
    print(f"get_sum1完成时间: {time.time()}, 结果: {global_num}")

def get_sum2():
    global global_num
    for i in range(10000000):
        global_num += 1
    print(f"get_sum1完成时间: {time.time()}, 结果: {global_num}")


if __name__ == "__main__":
    t1 = threading.Thread(target=get_sum1)
    t2 = threading.Thread(target=get_sum2)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("主线程执行完毕")


# 在你的电脑上，操作系统或 Python 的线程调度器可能倾向于让 t1（运行 get_sum1）先开始并执行一段时间，然后 t2（运行 get_sum2）才开始显著运行。
# 如果 t1 在 t2 开始前已经完成了一部分累加（比如累加到 1000 万以上），而 t2 随后接手并继续累加到 2000 万，那么：
# get_sum1 打印时，global_num 已经超过了 1000 万（但可能还未到 2000 万）。
# get_sum2 在完成后总是打印 2000 万，因为它执行了剩余的累加。