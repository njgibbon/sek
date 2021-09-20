from ....core.check import CoreCheck
from ....core.enums import CheckResult
from ....aws.utils import unrestricted_security_groups_ingress


class ServiceSecurityGroupsCheck(CoreCheck):
    def __init__(self, resource_name, context):
        super().__init__(resource_name, context)
        self.cloud = "aws"
        self.resource = "eks"
        self.name = "service-security-groups"

    def scan_logic(self):
        sg_ingress_status = unrestricted_security_groups_ingress(self.context.service_security_groups)
        if sg_ingress_status is False:
            self.result = CheckResult.PASS
        else:
            self.result = CheckResult.FAIL
