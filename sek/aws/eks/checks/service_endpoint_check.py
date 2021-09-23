from ....core.check import CoreCheck
from ....core.enums import CheckResult


class ServiceEndpointCheck(CoreCheck):
    def __init__(self, resource_name, context, skip):
        super().__init__(resource_name, context, skip)
        self.cloud = "aws"
        self.resource = "eks"
        self.name = "service-endpoint"

    def scan_logic(self):
        endpoint_public_access = self.context.cluster_description["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"]
        if endpoint_public_access is False:
            self.result = CheckResult.PASS
            return
        self.result = CheckResult.FAIL
        return
