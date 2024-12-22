def fun_A():
    print("This is fun_A")

def fun_B():
    print('-'*40)
    print("This is fun_B")
    fun_A()
    print('-'*40)

fun_B()