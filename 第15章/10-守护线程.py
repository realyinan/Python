import threading, time

def work():
    for i in range(10):
        print(f"第{i}天上班")
        time.sleep(0.2)


if __name__ == "__main__":
    t1 = threading.Thread(target=work, daemon=True)
    t1.start()
    time.sleep(1)
    print("主线程结束")
