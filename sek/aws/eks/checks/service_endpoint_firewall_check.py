from ....core.check import CoreCheck
from ....core.enums import CheckResult


class ServiceEndpointFirewallCheck(CoreCheck):
    def __init__(self, resource_name, context, skip):
        super().__init__(resource_name, context, skip)
        self.cloud = "aws"
        self.resource = "eks"
        self.name = "service-endpoint-firewall"

    def scan_logic(self):
        endpoint_public_access = self.context.cluster_description["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"]
        if endpoint_public_access:
            public_access_cidrs = self.context.cluster_description["cluster"]["resourcesVpcConfig"]["publicAccessCidrs"]
            for ipv4_range in public_access_cidrs:
                if ipv4_range == "0.0.0.0/0":
                    self.result = CheckResult.FAIL
                    return
        self.result = CheckResult.PASS
        return
