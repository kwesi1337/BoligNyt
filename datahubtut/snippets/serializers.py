import json

import pika
from rest_framework import serializers

from snippets import config as cfg
from snippets.models import Snippet

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=cfg.RABBIT_HOST))

channel = connection.channel()

channel.queue_declare(queue=cfg.QUEUE_TOPIC)

fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

message = json.dumps(fields)
channel.basic_publish(exchange='',
                      routing_key=cfg.QUEUE_TOPIC, body=message)
print(" [x] sent data to RabbitMQ")
connection.close()


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:

        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


    def create(self, validated_data):
        """
        Create and return a new 'Snippet' instance, given the validated data.
        """

        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Snippet' instance, given the validated data.
        """

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.lineos = validated_data.get('lineos', instance.lineos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

