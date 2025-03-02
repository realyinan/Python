import multiprocessing
import multiprocessing.process
import time


# target—表示调用对象，即子进程要执行的任务（回调函数入口地址）
# args—表示以元组的形式向子任务函数传参，元组方式传参一定要和参数的顺序保持一致
# kwargs—表示以字典的方式给子任务函数传参，字典方式传参字典中的key要和参数名保持一致
# name—为子进程的名称


def coding(name, num):
    for i in range(num):
        print(f"{name}正在敲第{i}行代码")
        time.sleep(0.2)

def music(name, count):
    for i in range(count):
        print(f"{name}正在听第{i}首音乐")
        time.sleep(0.2)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=coding, name="A", args=("小明", 10))
    p2 = multiprocessing.Process(target=music, name="B", kwargs={"count": 10, "name": "小明"})

    print(p1.name)
    print(p2.name)

    p1.start()
    p2.start()
