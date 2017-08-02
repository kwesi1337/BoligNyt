import json

import pika
import snippets.test.config as cfg

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=cfg.RABBIT_HOST))

channel = connection.channel()

channel.queue_declare(queue=cfg.QUEUE_TOPIC)

data = {
    "id": 1,
    "name":"My Name",
    "description": "Test JSON DATA"
}
message = json.dumps(data)
channel.basic_publish(exchange='',
                      routing_key=cfg.QUEUE_TOPIC, body=message)
print(" [x] sent data to RabbitMQ")
connection.close()
