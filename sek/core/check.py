from abc import abstractmethod

from .enums import CheckResult


class CoreCheck():
    def __init__(self, resource_name, context, skip):
        self.cloud = None
        self.resource = None
        self.resource_name = resource_name
        self.name = None
        self.result = None
        self.message = None
        self.context = context
        self.skip = skip

    def scan(self):
        if self.name in self.skip:
            self.result = CheckResult.SKIP
            return
        try:
            self.scan_logic()
        except Exception as err:
            self.result = CheckResult.ERROR
            self.message = str(type(err)) + " " + str(err)

    @abstractmethod
    def scan_logic(self):
        pass
