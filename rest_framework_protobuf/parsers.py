from django.core.exceptions import ImproperlyConfigured
from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser


class ProtobufParser(BaseParser):
    """Parses Protobuf-serialized data."""

    media_type = "application/x-google-protobuf"

    def parse(self, stream, media_type=None, parser_context=None):
        protobuf_cls = (parser_context or {}).get("protobuf_cls")

        if not protobuf_cls:
            raise ImproperlyConfigured(
                "`ProtobufParser` needs a `protobuf_cls` attribute in the `parser_context`."
            )

        try:
            obj = protobuf_cls()
            obj.ParseFromString(stream)
            return {k.name: v for k, v in obj.ListFields()}
        except Exception as exc:
            raise ParseError("Protobuf parse error - %s" % str(exc)) from exc
