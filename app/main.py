from faststream import FastStream
from faststream.kafka import KafkaBroker

kafka_broker = KafkaBroker("kafka1:19092")
app = FastStream(kafka_broker)

@kafka_broker.subscriber("user-events")
async def process_user_event(message):
    print(f"Received message: {message}")

if __name__ == "__main__":
    app.run()

