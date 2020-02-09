import pytest
from django.core.exceptions import ImproperlyConfigured

from rest_framework_protobuf.parsers import ProtobufParser

from .proto3 import addressbook_pb2


def test_parse_simple():
    data = b"\n\tTest Name\x10*\x1a\x11testname@test.com"

    parser = ProtobufParser()
    obj = parser.parse(data, parser_context={"protobuf_cls": addressbook_pb2.Person},)
    assert obj == {
        "name": "Test Name",
        "id": 42,
        "email": "testname@test.com",
    }


def test_missing_protobuf_cls():
    parser = ProtobufParser()
    with pytest.raises(ImproperlyConfigured):
        parser.parse(
            "", parser_context=None,
        )
