import pika
import ssl
import certifi
from urllib.parse import urlparse


class Sensor: #* This is the Producer
    def __init__(self, url):
        self.url = url
        self.params = pika.URLParameters(self.url)
        self.params.socket_timeout = 5  # Optional: Set a timeout
        self.parsed_url = urlparse(self.url)
        self.hostname = self.parsed_url.hostname
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())
        self.params.ssl_options = pika.SSLOptions(self.ssl_context, self.hostname)
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()

    def send_message(self, queue, message):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_publish(exchange='',
                      routing_key=queue,
                      body=message)
        self.connection.close()
        return f" [x] Sent '{message}'"

    def close(self):
        self.connection.close()