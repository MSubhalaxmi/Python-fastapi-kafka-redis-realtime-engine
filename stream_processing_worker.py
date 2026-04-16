from kafka import KafkaConsumer
import json
import redis

consumer = KafkaConsumer("vehicle-stream", bootstrap_servers="kafka:9092")
r = redis.Redis(host="redis", port=6379)

for msg in consumer:
    data = json.loads(msg.value)
    r.publish("live-telemetry", json.dumps(data))