from fastapi import APIRouter
from app.endpoints import video_stream
from app.endpoints import mqtt_test
from app.endpoints import import_csv
router=APIRouter()

router.include_router(video_stream.router)
router.include_router(mqtt_test.router)
router.include_router(import_csv.router)


