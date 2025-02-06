import logging

from dataclay.proxy import MiddlewareBase, MiddlewareException

logger = logging.getLogger(__name__)


class JohnCanOnlyRead(MiddlewareBase):
    def CallActiveMethod(self, request, context):
        metadata = dict(context.invocation_metadata())
        if metadata.get("username") == "john":
            raise MiddlewareException("John can only read, not call methods")

    def GetObjectAttribute(self, request, context):
        # Always allowed
        pass

    def SetObjectAttribute(self, request, context):
        metadata = dict(context.invocation_metadata())
        if metadata.get("username") == "john":
            raise MiddlewareException("John cannot set attributes")

    def DelObjectAttribute(self, request, context):
        metadata = dict(context.invocation_metadata())
        if metadata.get("username") == "john":
            raise MiddlewareException("John cannot delete attributes")

class JamesCanDoAgeThings(MiddlewareBase):
    ...
