from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import cv2
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./app/template")

some_file_path = "video2.mp4"
app = FastAPI()


def gen(vc):
    while True:
        rval, frame = vc.read()
        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

@app.get('/')
def home(request:Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": "id"})
    
@app.get("/api/v1/video/stream/{camera_id}")
def video_stream(camera_id: int):

    vc=cv2.VideoCapture(camera_id)
    return StreamingResponse(gen(vc), media_type="multipart/x-mixed-replace;boundary=frame")


