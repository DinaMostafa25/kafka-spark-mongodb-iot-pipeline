from faker import Faker
import random
from datetime import datetime


fake = Faker()

def generate_sensor_data():
    return {
        "sensor_id": f"M{random.randint(100,999)}",
        "machine_type": random.choice([
            "CNC",
            "Lathe",
            "Drill",
            "Conveyor"
        ]),
        "temperature": round(random.uniform(20, 50), 2),
        "humidity": round(random.uniform(30, 80), 2),
        "vibration": round(random.uniform(0.1, 1.0), 2),
        "power_consumption": random.randint(1000, 5000),
        "worker_id": f"W{random.randint(1,50)}",
        "safety_helmet": random.choice([True, False]),
        "status": random.choice([
            "running",
            "idle",
            "maintenance"
        ]),
        "timestamp": datetime.now().isoformat()
    }

data = generate_sensor_data()

# print(json.dumps(data, indent=2))

# while True:
#     print(generate_sensor_data())