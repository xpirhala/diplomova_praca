from fastapi_mqtt import FastMQTT, MQTTConfig
from fastapi import APIRouter
router= APIRouter()

mqtt_config = MQTTConfig(host='127.0.0.1',port=1883)

fast_mqtt = FastMQTT(
    config=mqtt_config
)


@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    fast_mqtt.client.subscribe("/mqtt") #subscribing mqtt topic 
    fast_mqtt.client.subscribe("/mqtt2")
    fast_mqtt.client.subscribe("/mqtt3")
    print("Connected: ", client, flags, rc, properties)

@fast_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ",topic, payload.decode(

    ), qos, properties)
    return 0

@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

@fast_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)


@router.get("/api/v1/publish/{message}")
async def func(message:str):
    fast_mqtt.publish("/mqtt3", message) #publishing mqtt topic 

    return {"result": True,"message":"Published" }
