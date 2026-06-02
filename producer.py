from kafka import KafkaProducer
from data_generator import generate_sensor_data
import json
import time



producer = KafkaProducer(
    bootstrap_servers=[
        "localhost:9094",
        "localhost:9095",
        "localhost:9096"
    ],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


#################################

def send_message():
   while True:
    data = generate_sensor_data()

    producer.send(
        "factory-sensors",
        value=data
    )

    producer.flush()

    print("Sent:", data)

    time.sleep(5)


send_message()