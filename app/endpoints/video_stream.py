from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import cv2
from app.core.decode_qr import decode

router= APIRouter()

def gen(vc):
    while True:
        rval, frame = vc.read()
        decode(frame)
        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')



@router.get("/api/v1/video/stream/{camera_id}")
def video_stream(camera_id: int):

    vc=cv2.VideoCapture(camera_id)
    return StreamingResponse(gen(vc), media_type="multipart/x-mixed-replace;boundary=frame")

from ximea import xiapi
import cv2
import PIL.Image
import matplotlib.pyplot as plt
import numpy   
from app.core.camera_handler import geter
@router.get("/api/v1/video/stream/ximea")
def video_stream():
    data=geter().camera.get_frame()
    print(numpy.size(open_cv_image))
    image=PIL.Image.fromarray(data, 'RGB')
    open_cv_image = numpy.array(image)
    
    return StreamingResponse(gen(open_cv_image), media_type="multipart/x-mixed-replace;boundary=frame")

