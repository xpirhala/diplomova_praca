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






fast_mqtt.init_app(app)




