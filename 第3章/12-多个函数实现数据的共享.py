students = []

def fun_A():
    global students
    students.append("张三")
    students.append("李四")
    students.append("王五")

def fun_B():
    for i in students:
        print(i)

fun_A()
fun_B()