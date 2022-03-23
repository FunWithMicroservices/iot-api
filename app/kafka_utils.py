import io
import json
import avro.schema
import avro.io

from settings import KAFKA_PRODUCER


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
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        self._writer.write(self.__dict__, encoder)
        return bytes_writer.getvalue()

    def produce(self):
        KAFKA_PRODUCER.produce(self._topic_name, self.to_avro())
        KAFKA_PRODUCER.flush()
