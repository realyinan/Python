import os
import time

os.rename('./第4章/python.txt', './第4章/linux.txt')
time.sleep(5)
os.remove('./第4章/linux.txt')

