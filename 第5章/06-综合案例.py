import time

try:
    f = open('./第5章/python.txt', 'r', encoding='utf-8')
    try:
        while True:
            con = f.read(3)
            if len(con) == 0:
                break
            print(con)
            time.sleep(3)
    except:
        print("读取异常")
    finally:
        f.close()
        print("关闭文件")
except:
    print("文件不存在")