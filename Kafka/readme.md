Apache Kafka

from kafka import KafkaConsumer

def consume_messages():
    consumer = KafkaConsumer('test',
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=1000)

    for message in consumer:
        print(message.value.decode('utf-8'))

if __name__ == '__main__':
    consume_messages()
