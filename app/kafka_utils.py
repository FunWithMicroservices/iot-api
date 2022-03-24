import io
import json
import logging
import avro.schema
import avro.io

from settings import KAFKA_PRODUCER


logger = logging.getLogger(__name__)


class KafkaAvroMixin:
    type_mapper = {
        "str": "string",
        "int": "int",
        "float": "float"
    }

    @property
    def _avro_schema(self):
        schema = self._get_schema_dict()
        return avro.schema.parse(json.dumps(schema))

    @property
    def _writer(self):
        return avro.io.DatumWriter(self._avro_schema)

    @property
    def _topic_name(self):
        return f"iot-{type(self).__name__.lower()}-data"

    def _get_schema_dict(self):
        return {
            "namespace": "iot",
            "type": "record",
            "name": type(self).__name__,
            "fields": [
                {"name": name, "type": KafkaAvroMixin.type_mapper[dtype.__name__]}
                for name, dtype in self.__annotations__.items()
            ]
        }

    def to_avro(self):
        logger.info(f"Convert {type(self).__name__} Obj to avro: {self.__dict__}")
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        self._writer.write(self.__dict__, encoder)
        return bytes_writer.getvalue()

    def produce(self):
        KAFKA_PRODUCER.produce(self._topic_name, self.to_avro())
        logger.info(f"Produce {type(self).__name__} and send to {self._topic_name}")
        KAFKA_PRODUCER.flush()
