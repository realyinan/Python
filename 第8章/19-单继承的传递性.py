class C():
    def func(self):
        print("C类中的方法")

class B(C):
    pass

class A(B):
    pass


a = A()
a.func()