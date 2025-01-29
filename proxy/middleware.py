import logging

from dataclay.proxy import MiddlewareBase, MiddlewareException

logger = logging.getLogger(__name__)


class ActiveMethodWhitelist(MiddlewareBase):
    def __init__(self, user, methods):
        self._user = user
        self._method_names = methods

    def CallActiveMethod(self, request, context):
        metadata = dict(context.invocation_metadata())
        if ...:
            # Not the user we filter
            return

        if ...:
            # Method in whitelist
            return

        raise MiddlewareException("Method not allowed")

    def GetObjectAttribute(self, request, context):
        metadata = dict(context.invocation_metadata())

        if metadata.get("username") != self._user:
            # Not the user we filter
            return

        gets = ("get", "__getattribute__", "getattr")
        for method in gets:
            if method in self._method_names:
                # Method in whitelist
                return 

        raise MiddlewareException("Method GetObjectAttribute not allowed")

    def SetObjectAttribute(self, request, context):
        ...
        sets = ("set", "__setattr__", "setattr")
        ...

        raise MiddlewareException("Method SetObjectAttribute not allowed")

    def DelObjectAttribute(self, request, context):
        ...
        dels = ("delete", "__delattr__", "delattr")
        ...

        raise MiddlewareException("Method DelObjectAttribute not allowed")
