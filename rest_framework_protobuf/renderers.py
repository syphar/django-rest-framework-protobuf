from django.core.exceptions import ImproperlyConfigured
from rest_framework.renderers import BaseRenderer


class ProtobufRenderer(BaseRenderer):
    """Renderer which serializes to Protobuf."""

    media_type = "application/x-google-protobuf"
    format = "protobuf"
    render_style = "binary"
    charset = None

    def render(self, data, media_type=None, renderer_context=None):
        protobuf_cls = (renderer_context or {}).get("protobuf_cls")

        if not protobuf_cls:
            raise ImproperlyConfigured(
                "`ProtobufRenderer` needs a `protobuf_cls` attribute in the `renderer_context`."
            )

        obj = protobuf_cls()

        for key, value in data.items():
            setattr(obj, key, value)

        return obj.SerializeToString()
