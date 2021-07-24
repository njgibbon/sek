from abc import ABC, abstractmethod


class CoreCheck(): 
    def __init__(self, resource_name, context):
        self.cloud = None
        self.resource = None
        self.resource_name = resource_name
        self.name = None
        self.result = None
        self.message = None
        self.context = context

    @abstractmethod
    def scan(self):
        pass
