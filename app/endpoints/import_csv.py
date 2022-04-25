from fastapi_mqtt import FastMQTT, MQTTConfig
from fastapi import APIRouter, UploadFile
from app.core.cache import get_cache_class

router= APIRouter()


@router.post('/api/v1/import/csv')
def import_csv(file: UploadFile):

    get_cache_class().upload_csv(file)

    print(get_cache_class().need_to_be_loaded)
    return {"d":"s"}