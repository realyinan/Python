# 请实现一个装饰器，每次调用函数时，将函数名字及调用函数的时间点写入文件中。
import time

def decorator(fn):
    run_time = None
    def inner(*args, **kwargs):
        nonlocal run_time
        run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        fn(*args, **kwargs)
        f = open(f"第9章/日志.log", 'a', encoding='utf-8')
        f.write(f"{fn.__name__}函数于{run_time}运行.\n")
        f.close()
    return inner


@decorator
def func(*args, **kwargs):
    pass


func()
time.sleep(0.5)
func()
time.sleep(0.5)
func()
time.sleep(0.5)
func()
time.sleep(0.5)

