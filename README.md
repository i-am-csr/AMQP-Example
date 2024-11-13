# AMQP Example
This is a simple example of how to use AMQP with CloudAMPQ using Python.

## Usage
1. Install the required packages:
```bash
pip install -r requirements.txt
```
2. Set the environment variables:
```bash
export CLOUDAMQP_URL=your_cloudamqp_url
```
3. Run the producer:
```bash
python producer.py
```
4. Run the consumer:
```bash
python consumer.py
```

## Explanation
This program simulates a producer and a consumer. The producer sends a message to the queue and the consumer receives it.
This is a simple example of sending and receiving messages using AMQP with CloudAMPQ.
The messages are sent and received are a simulation of a temperature and humidity sensors.
In a real scenario, having this data, we could store it in a database, send it to a dashboard, or even trigger an alert if the values are out of the expected range.