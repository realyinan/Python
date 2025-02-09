def check(fn):
    def inner():
        print("请登录")
        fn()
    return inner

@check
def comment():
    print("发表评论")


comment()