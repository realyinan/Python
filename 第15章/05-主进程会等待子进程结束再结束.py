import time, multiprocessing

def work():
    for i in range(10):
        print(f"第{i}天上班")
        time.sleep(0.2)



if __name__ == "__main__":
    p1 = multiprocessing.Process(target=work)
    p1.start()
    time.sleep(1)
    print("主进程结束")