import config as cfg
import pika
import json

class producer:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=cfg.QUEUE_TOPIC)
    print("we are here!")

    def produceQueue(message):
        producer.channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=message)
        print(message, "< sent to RabbitMQ")

    def closeConnection(self):
        producer.connection.close()

