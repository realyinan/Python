try:
    print(name)
    print(10/0)
except (NameError, ZeroDivisionError):
    print("出现异常")