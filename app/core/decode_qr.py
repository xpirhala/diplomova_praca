
import cv2
import pyzbar.pyzbar as pyzbar
from app.schemas.mqtt_message import MqttMessage
from app.endpoints.mqtt_test import fast_mqtt

def decode(im) :
  # Find barcodes and QR codes
  im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  decodedObjects = pyzbar.decode(im)
  
  # Print results
  for obj in decodedObjects:
    message=MqttMessage(truck_id="1234",qr_code=obj.data)
    fast_mqtt.publish("/mqtt3", message.json())

  return decodedObjects