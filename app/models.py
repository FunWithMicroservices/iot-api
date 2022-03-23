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


if __name__ == "__main__":
    from datetime import datetime
    obj = {
        "car_id": "abc",
        "lat": 1.234,
        "long": 12.75,
        "timestamp": int(datetime.now().timestamp())
    }
    data = Location(**obj)
    data.produce()
    print()
