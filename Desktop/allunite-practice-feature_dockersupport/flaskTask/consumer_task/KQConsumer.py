from kafka import KafkaConsumer

import flaskTask.web_app.config as cfg


def consumer():
    KQConsumer = KafkaConsumer(bootstrap_servers=str(cfg.KAFKA_HOST),
                             auto_offset_reset='earliest')
    KQConsumer.subscribe([cfg.QUEUE_TOPIC])
    print(cfg.KAFKA_HOST)
    print(cfg.QUEUE_TOPIC)
    print("listening for publishers")
    for message in KQConsumer:
        print(message)

consumer()