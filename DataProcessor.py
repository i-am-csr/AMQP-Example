import pika
import ssl
import certifi
from urllib.parse import urlparse


class DataProcessor:  #* This is the Consumer
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

    def callback(self, ch, method, properties, body):
        message = eval(body.decode())
        temperature = message.get("temperature")
        humidity = message.get("humidity")

        if temperature is not None and temperature > 28:
            print(f"[ALERT] High temperature detected: {temperature}°C")

        if humidity is not None and humidity < 35:
            print(f"[ALERT] Low humidity detected: {humidity}%")

        if temperature is not None and humidity is not None:
            print(f"Received both temperature and humidity: {temperature}°C, {humidity}%")

    def consume(self, queue):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_consume(queue=queue, on_message_callback=self.callback, auto_ack=True)
        print(f" [*] Waiting for messages in '{queue}'. To exit press CTRL+C")
        self.channel.start_consuming()
