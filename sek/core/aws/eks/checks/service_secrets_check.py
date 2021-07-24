from ..aws_eks_check import AWSEKSCheck


class ServiceSecretsCheck(AWSEKSCheck):
    def __init__(self, resource_name, context):
        super().__init__(resource_name, context)
        self.name = "service-secrets"

    def scan(self):
        self.result = "PASS"
