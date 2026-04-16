from fastapi import FastAPI
from kafka import KafkaProducer
import json

app = FastAPI()
producer = KafkaProducer(bootstrap_servers="kafka:9092")

@app.post("/vehicle/telemetry")
async def ingest_data(payload: dict):
    producer.send("vehicle-stream", json.dumps(payload).encode())
    return {"status": "streamed"}