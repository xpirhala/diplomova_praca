from functools import lru_cache
from fastapi import UploadFile, HTTPException
import pandas as pd
from app.schemas.mqtt_message import MqttMessage

class SingletonCache():
    correct_loaded_qr_codes:list = []
    wrong_loaded_qr_codes:list = []
    need_to_be_loaded:list = []
    truck_id:str

    def upload_csv(self, file: UploadFile):

        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=415, detail="This media type is not supported! File should be CSV.")
        self.need_to_be_loaded=[]
        df = pd.read_csv(file.file,sep=",")

        for index, row in df.iterrows():
            csv = MqttMessage(**row)
            self.need_to_be_loaded.append(csv.qr_code)
            self.truck_id=csv.truck_id
        
        


@lru_cache
def get_cache_class():
    return SingletonCache()