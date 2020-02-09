import pytest
from django.core.exceptions import ImproperlyConfigured

from rest_framework_protobuf.renderers import ProtobufRenderer

from .proto3 import addressbook_pb2


def test_render_simple():
    obj = {
        "name": "Test Name",
        "id": 42,
        "email": "testname@test.com",
    }

    renderer = ProtobufRenderer()
    content = renderer.render(
        obj, renderer_context={"protobuf_cls": addressbook_pb2.Person},
    )
    assert content == b"\n\tTest Name\x10*\x1a\x11testname@test.com"


def test_render_unknown_field():
    obj = {
        "unknown_field": "raises an error",
    }

    renderer = ProtobufRenderer()
    with pytest.raises(AttributeError):
        renderer.render(
            obj, renderer_context={"protobuf_cls": addressbook_pb2.Person},
        )


def test_missing_protobuf_cls():
    renderer = ProtobufRenderer()
    with pytest.raises(ImproperlyConfigured):
        renderer.render(
            {}, renderer_context=None,
        )
