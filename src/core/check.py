from abc import ABC, abstractmethod

class Check(object): 
    def __init__(self, context):
        print("Check")
        self.cloud = None
        self.resource = None
        self.resource_name = None
        self.name = None
        self.result = None
        self.message = None
        self.context = context

    @abstractmethod
    def scan(self):
        pass
