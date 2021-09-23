from ....core.check import CoreCheck
from ....core.enums import CheckResult


class ServiceSecretsCheck(CoreCheck):
    def __init__(self, resource_name, context, skip):
        super().__init__(resource_name, context, skip)
        self.cloud = "aws"
        self.resource = "eks"
        self.name = "service-secrets"

    def scan_logic(self):
        cluster = self.context.cluster_description.get("cluster")
        encryption_config = cluster.get("encryptionConfig")
        if encryption_config is None:
            self.result = CheckResult.FAIL
            return
        for config in encryption_config:
            resources = config.get("resources")
            for resource in resources:
                if resource == "secrets":
                    self.result = CheckResult.PASS
                    return
        self.result = CheckResult.FAIL
        return
