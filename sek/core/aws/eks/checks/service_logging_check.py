from ..aws_eks_check import AWSEKSCheck


class ServiceLoggingCheck(AWSEKSCheck):
    def __init__(self, resource_name, context):
        super().__init__(resource_name, context)
        self.name = "service-logging"

    def scan(self):
        log_types = ["audit", "api", "authenticator", "controllerManager", "scheduler"]
        all_log_types_found = False
        if all(item in self.context.cluster_description["cluster"]["logging"]["clusterLogging"][0]["types"] for item in log_types):
            all_log_types_found = True
        if all_log_types_found == True:
            self.result = "PASS"
        else:
            self.result = "FAIL"
