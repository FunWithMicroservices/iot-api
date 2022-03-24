import os
import logging
from pathlib import Path
from confluent_kafka import Producer, SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


BASE_DIR = Path(__file__).resolve(strict=True).parent
LOG_DIR = BASE_DIR / "logs"

KAFKA_PRODUCER = Producer(**{
    "bootstrap.servers": os.environ["KAFKA_HOST"]
})

SCHEMA_REGISTRY_URL = os.environ["SCHEMA_REGISTRY_URL"]
