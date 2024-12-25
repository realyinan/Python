def num(*args, **kwargs):
    for i in args:
        print(i)
    for k, v in kwargs.items():
        print(f"k:{k}, v:{v}")

num(1, 2, 3, 4, name='python', age=20)
