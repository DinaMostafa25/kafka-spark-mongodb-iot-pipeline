# Kafka-Spark-MongoDB IoT Pipeline

## Project Overview

This project simulates a smart factory environment where industrial machines continuously generate telemetry data.

Using Python, Kafka, and Spark Structured Streaming, the pipeline collects and processes real-time events containing machine metrics, worker information, safety indicators, and operational status.

The processed data will eventually be stored in MongoDB for analytics and monitoring use cases such as:

- Machine health monitoring
- Predictive maintenance
- Worker safety tracking
- Power consumption analysis
- Operational efficiency reporting

---

## Architecture

```text
Faker Data Generator
        │
        ▼
Kafka Producer
        │
        ▼
Apache Kafka Cluster (3 Brokers)
        │
        ▼
PySpark Structured Streaming Consumer
        │
        ▼
MongoDB (Coming Next)
```

---

## Technologies Used

- Python
- Faker
- Apache Kafka
- Kafka UI
- PySpark Structured Streaming
- Docker Compose
- Git & GitHub

---

## Project Structure

```text
.
├── data_generator.py     # Generates fake IoT sensor data
├── producer.py           # Sends sensor data to Kafka
├── consumer.py           # Reads streaming data from Kafka using Spark
├── docker-compose.yml    # Kafka cluster and Kafka UI
├── .gitignore
└── README.md
```

---

## Implemented Features

### 1. Fake IoT Data Generation

Sensor events are generated using the Faker library.

Example event:

```json
{
  "sensor_id": "M542",
  "machine_type": "CNC",
  "temperature": 34.75,
  "humidity": 62.41,
  "vibration": 0.56,
  "power_consumption": 3120,
  "worker_id": "W18",
  "safety_helmet": true,
  "status": "running",
  "timestamp": "2026-06-02T16:05:30.123456"
}
```
---
Generated Fields:

| Field | Description |
|---------|------------|
| sensor_id | Unique machine identifier |
| machine_type | Machine category (CNC, Lathe, Drill, Conveyor) |
| temperature | Machine temperature in °C |
| humidity | Environmental humidity percentage |
| vibration | Machine vibration level |
| power_consumption | Power consumption in watts |
| worker_id | Worker assigned to the machine |
| safety_helmet | Whether the worker is wearing a helmet |
| status | Machine status (running, idle, maintenance) |
| timestamp | Event generation timestamp |

---

### 2. Kafka Producer

The producer:

- Generates IoT events
- Converts them to JSON
- Publishes them to a Kafka topic

Topic used:

```text
iot-sensors
```

---

### 3. Kafka Cluster

A Kafka cluster was deployed using Docker Compose with:

- 3 Kafka Brokers
- KRaft mode (ZooKeeper-free)
- Kafka UI for monitoring

Broker Endpoints:

```text
localhost:9094
localhost:9095
localhost:9096
```

Kafka UI:

```text
http://localhost:12000
```

---

### 4. Spark Structured Streaming Consumer

The consumer:

- Connects to Kafka
- Reads messages from the `iot-sensors` topic
- Streams data continuously
- Displays incoming records in real time

Current output:

```text
+--------------------+
|value               |
+--------------------+
|{"sensor_id":"M501"...}
+--------------------+
```

---

## Current Progress

### Completed

-  Data Generator
-  Kafka Producer
-  Kafka Cluster
-  Kafka UI
-  Spark Structured Streaming Consumer
-  GitHub Repository

### In Progress

- [ ] JSON Parsing in Spark
- [ ] Data Transformations
- [ ] MongoDB Integration
- [ ] Data Persistence
- [ ] Analytics Layer

---

## Running the Project

### 1. Start Kafka Cluster

```bash
docker-compose up -d
```

### 2. Start the Producer

```bash
python producer.py
```

### 3. Start the Spark Consumer

```bash
python consumer.py
```

### 4. Monitor Kafka

Open Kafka UI:

```text
http://localhost:12000
```

---

## Future Enhancements

- Store processed sensor data in MongoDB
- Add data quality checks
- Create aggregation pipelines
- Build dashboards for monitoring sensor metrics
- Containerize Spark jobs
- Deploy the complete pipeline in the cloud

---

## Learning Objectives

This project provides hands-on experience with:

- Real-time data streaming
- Apache Kafka producers and consumers
- Spark Structured Streaming
- NoSQL databases
- End-to-end data engineering workflows
- Event-driven architectures

