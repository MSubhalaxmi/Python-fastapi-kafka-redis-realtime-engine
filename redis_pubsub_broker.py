import redis

r = redis.Redis(host="redis", port=6379)

def publish_alert(channel, message):
    r.publish(channel, message)

def subscribe(channel):
    pubsub = r.pubsub()
    pubsub.subscribe(channel)
    return pubsub.listen()