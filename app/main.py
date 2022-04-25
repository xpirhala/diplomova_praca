from functools import lru_cache
from typing import Any
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import cv2
from fastapi.templating import Jinja2Templates
from app.endpoints import apis
from app.endpoints.mqtt_test import fast_mqtt
templates = Jinja2Templates(directory="./app/template")


app = FastAPI()

app.include_router(apis.router)

from app.core import ximea
class Recorder():
    def __init__(self):
        self.setupUi(self)
        xiC = ximea.XiCMonoConfig()
        self.camera = ximea.XimeaCamera(xiC.get_instance())

@lru_cache
def geter():
    record=Recorder()

@app.get('/')
def home(request:Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": "id"})



fast_mqtt.init_app(app)




