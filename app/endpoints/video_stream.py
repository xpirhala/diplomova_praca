from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import cv2


router= APIRouter()

def gen(vc):
    while True:
        rval, frame = vc.read()
        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')



@router.get("/api/v1/video/stream/{camera_id}")
def video_stream(camera_id: int):

    vc=cv2.VideoCapture(camera_id)
    return StreamingResponse(gen(vc), media_type="multipart/x-mixed-replace;boundary=frame")
