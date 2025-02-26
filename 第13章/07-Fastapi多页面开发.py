from fastapi import FastAPI
from fastapi import Response
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()

app.mount("/images", StaticFiles(directory="第13章\Source\Beauty\images"), name="images")
app.mount("/css", StaticFiles(directory="第13章\Source\Beauty\css"), name="css")

@app.get("/Saaya.html")
def Saaya():
    with open("第13章\Source\Beauty\Saaya.html", "rb") as f:
        data = f.read()
    return Response(content=data, media_type="text/html")

@app.get("/Mikami.html")
def Mikami():
    with open("第13章\Source\Beauty\Mikami.html", 'rb') as f:
        data = f.read()
    return Response(content=data, media_type="text/html")


uvicorn.run(app=app, host="127.0.0.1", port=8000)