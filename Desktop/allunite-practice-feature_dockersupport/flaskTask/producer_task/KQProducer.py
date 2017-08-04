


from kafka import KafkaProducer
import threading, time
class kproducer(threading.Thread):
    daemon = True
    Kprod = KafkaProducer(bootstrap_servers='localhost')
    def produceQueue(topic, message):
        kproducer.Kprod.send(topic, message)
        time.sleep(1)

