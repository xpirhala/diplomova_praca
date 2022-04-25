from pydantic import BaseModel

class MqttMessage(BaseModel):
    truck_id:str
    qr_code: str
