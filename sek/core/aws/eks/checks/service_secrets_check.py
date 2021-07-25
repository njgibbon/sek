from ..aws_eks_check import AWSEKSCheck
from ....core_enums import CheckResult

class ServiceSecretsCheck(AWSEKSCheck):
    def __init__(self, resource_name, context):
        super().__init__(resource_name, context)
        self.name = "service-secrets"

    def scan_logic(self):
        encryption_config = self.context.cluster_description["cluster"].get("encryptionConfig")
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

