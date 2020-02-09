from rest_framework_protobuf.parsers import ProtobufParser
from rest_framework_protobuf.renderers import ProtobufRenderer

from .proto3 import addressbook_pb2


def test_render_and_parse():
    obj = {
        "name": "Test Name",
        "id": 42,
        "email": "testname@test.com",
    }

    context = {"protobuf_cls": addressbook_pb2.Person}

    renderer = ProtobufRenderer()
    content = renderer.render(obj, renderer_context=context,)

    parser = ProtobufParser()
    new_obj = parser.parse(content, parser_context=context)

    assert new_obj == obj
