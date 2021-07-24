from ...core_check import CoreCheck


class AWSEKSCheck(CoreCheck): 
    def __init__(self, resource_name, context):
        super().__init__(resource_name, context)
        self.cloud = "aws"
        self.resource = "eks"
