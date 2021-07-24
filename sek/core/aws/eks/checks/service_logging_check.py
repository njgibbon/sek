from ..aws_eks_check import AWSEKSCheck


class ServiceLoggingCheck(AWSEKSCheck):
    def __init__(self, resource_name, context):
        super().__init__(resource_name, context)
        self.name = "service-logging"

    def scan(self):
        self.result = "PASS"
