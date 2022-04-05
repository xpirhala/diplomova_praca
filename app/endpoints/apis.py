from fastapi import APIRouter
from app.endpoints import video_stream
from app.endpoints import mqtt_test
router=APIRouter()

router.include_router(video_stream.router)
router.include_router(mqtt_test.router)



