import random

def generate_code(num):
    mystr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = ""
    for i in range(num):
        code += mystr[random.randint(0, len(mystr)-1)]
    return code

print(generate_code(5))
