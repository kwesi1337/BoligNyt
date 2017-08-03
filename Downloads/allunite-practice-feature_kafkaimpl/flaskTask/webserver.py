from flask import Flask, render_template, request, url_for
import json
from producer import producer
import config as cfg
from KQProducer import kproducer
app = Flask(__name__)



@app.route('/', methods=['POST'])
def jsonRequest():
    data = request.get_json()
    print(data)
    json_data = json.dumps(data)
    print(json_data)
    producer.produceQueue(json_data)
    kproducer.produceQueue("my-topic", str.encode(json_data))
    return "rabbit"


@app.route('/close/', methods=['GET'])
def close():
    producer.closeConnection()
    return "Connection to RabbitMQ was closed"


if __name__ == '__main__':
    app.run(
        debug=True,
        host=cfg.host_ip,
        port=cfg.host_port
    )
