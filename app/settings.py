import os
from pathlib import Path
from confluent_kafka import Producer, SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve(strict=True).parent

KAFKA_PRODUCER = Producer(**{
    "bootstrap.servers": os.environ["KAFKA_HOST"]
})

SCHEMA_REGISTRY_URL = os.environ["SCHEMA_REGISTRY_URL"]
