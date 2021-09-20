from ....core.check import CoreCheck
from ....core.enums import CheckResult


class ServiceLoggingCheck(CoreCheck):
    def __init__(self, resource_name, context):
        super().__init__(resource_name, context)
        self.cloud = "aws"
        self.resource = "eks"
        self.name = "service-logging"

    def scan_logic(self):
        cluster_logging = self.context.cluster_description["cluster"]["logging"]["clusterLogging"]
        for log_config in cluster_logging:
            if log_config.get("enabled") is False:
                self.result = CheckResult.FAIL
                return
        self.result = CheckResult.PASS
        return
