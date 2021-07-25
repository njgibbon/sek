from ..aws_eks_check import AWSEKSCheck
from ....core_enums import CheckResult

class ServiceLoggingCheck(AWSEKSCheck):
    def __init__(self, resource_name, context):
        super().__init__(resource_name, context)
        self.name = "service-logging"

    def scan_logic(self):
        cluster_logging = self.context.cluster_description["cluster"]["logging"]["clusterLogging"]
        for log_config in cluster_logging:
            if log_config.get("enabled") is False:
                self.result = CheckResult.FAIL
                return
        self.result = CheckResult.PASS

