# from fastapi import FastAPI
# from pydantic import BaseModel
# from faststream.kafka.fastapi import KafkaRouter
# 
# kafka_router = KafkaRouter("kafka1:19092")
# 
# app = FastAPI()
# app.include_router(kafka_router)
# 
# class UserEvent(BaseModel):
#     user_id: str
#     event_type: str
#     percent: int
# 
# @kafka_router.publisher("user-events")
# @app.post("/produce")
# async def produce_event(event: UserEvent):
#     message = {
#         "user_id": event.user_id,
#         "event_type": event.event_type,
#         "percent": event.percent,
#     }
#     print(f"Attempting to publish message: {message}")
#     return message
#

from fastapi import FastAPI
from pydantic import BaseModel
from faststream.kafka import KafkaBroker

kafka_broker = KafkaBroker("kafka1:19092")

app = FastAPI()

class UserEvent(BaseModel):
    user_id: str
    event_type: str
    percent: int

@app.on_event("startup")
async def startup_event():
    await kafka_broker.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await kafka_broker.disconnect()

@app.post("/produce")
async def produce_event(event: UserEvent):
    message = {
        "user_id": event.user_id,
        "event_type": event.event_type,
        "percent": event.percent,
    }
    print(f"Attempting to publish message: {message}")
    
    try:
        await kafka_broker.publish(message, topic="user-events")
        print("Message successfully published")
    except Exception as e:
        print(f"Failed to publish message: {e}")
    
    return {"status": "Message attempted"}

