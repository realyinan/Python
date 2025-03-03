import threading, time

global_num = 0
lock = threading.Lock()

def get_sum1():
    # 加锁
    lock.acquire()
    global global_num
    for i in range(10000000):
        global_num += 1
    print(f"get_sum1完成时间: {time.time()}, 结果: {global_num}")
    # 释放锁
    lock.release()

def get_sum2():
    with lock:
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


# 互斥锁: 对共享数据进行锁定，保证同一时刻只有一个线程去操作。
# 互斥锁是多个线程一起去抢，抢到锁的线程先执行，没有抢到锁的线程进行等待，等锁使用完释放后，其它等待的线程再去抢这个锁。
# 使用互斥锁的时候需要注意死锁的问题，未在合适的地方注意释放锁

