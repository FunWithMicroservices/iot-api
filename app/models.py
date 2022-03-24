from pydantic import BaseModel

from kafka_utils import KafkaAvroMixin


class Location(BaseModel, KafkaAvroMixin):
    car_id: str
    lat: float
    long: float
    timestamp: int


class Speed(BaseModel, KafkaAvroMixin):
    car_id: str
    value: int
    timestamp: int
