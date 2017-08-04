import os

########################################
if os.getenv("queue-topic"):
    QUEUE_TOPIC = os.environ.get("queue-topic")
else:
    QUEUE_TOPIC = "my-topic"
########################################
if os.getenv("rabbit-ip"):
    RABBIT_HOST = os.environ.get("rabbit-ip")
else:
    RABBIT_HOST = "localhost"
if os.getenv("rabbit-port"):
    port = os.environ.get("rabbit-port")
else:
    port = int("15672")
########################################
if os.getenv("kafka-ip"):
    KAFKA_HOST = os.environ.get("kafka-ip")
else:
    KAFKA_HOST = "localhost"
if os.getenv("kafka-port"):
    port = os.environ.get("kafka-port")
else:
    port = int("2181")
########################################
if os.getenv("WEBSERVER_IP"):
    host_ip = os.environ.get("WEBSERVER_IP")
else:
    host_ip = "0.0.0.0"
if os.getenv("WEBSERVER_PORT"):
    host_port = os.environ.get("WEBSERVER_PORT")
else:
    host_port = int("80")
########################################

print(host_ip)
