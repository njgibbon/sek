from ..aws_eks_check import AWSEKSCheck
from ....core.enums import CheckResult


class ServiceEndpointCheck(AWSEKSCheck):
    def __init__(self, resource_name, context):
        super().__init__(resource_name, context)
        self.name = "service-endpoint"

    def scan_logic(self):
        endpoint_public_access = self.context.cluster_description["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"]
        if (endpoint_public_access is False):
            self.result = CheckResult.PASS
            return
        else:
            self.result = CheckResult.FAIL
            return
