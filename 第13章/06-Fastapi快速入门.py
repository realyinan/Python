# 1. 导入模块
# 导入Fastapi类
from fastapi import FastAPI
# 导入Response类, 用于返回数据给浏览器端
from fastapi import Response
# 导入静态文件支持
from fastapi.staticfiles import StaticFiles
# 导入uvicorn服务器模块, 用于保持文件一直运行
import uvicorn


# 2. 创建Fastapi对象
app = FastAPI()

# 3. app挂载静态文件
app.mount("/images", StaticFiles(directory="第13章\Source\Beauty\images"), name="images")
app.mount("/css", StaticFiles(directory="第13章\Source\Beauty\css"), name="css")


# 3. 通过@app路由装饰器收发信息
@app.get("/")
def main():
    with open("第13章/Source/Beauty/Saaya.html", 'rb') as f:
        data = f.read()

    # 把data数据以text/html格式返回给浏览器端
    return Response(content=data, media_type='text/html')

# 4. 运行服务器
uvicorn.run(app=app, host="127.0.0.1", port=9000)