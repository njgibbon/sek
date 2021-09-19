import time

from ...core.runner import CoreRunner
from .aws_eks_context import AWSEKSContext
from .checks import *


class AWSEKSRunner(CoreRunner):
    def __init__(self, name):
        start_time = time.time()

        super().__init__(name)

        # Set AWS EKS related data
        self.link = "https://github.com/njgibbon/sek/blob/main/checks/aws/eks/readme.md"

        # Create AWS EKS Context
        self.context = AWSEKSContext(name)

        # Load AWS EKS Checks into the Runner
        service_logging_check = ServiceLoggingCheck(name, self.context)
        service_secrets_check = ServiceSecretsCheck(name, self.context)
        service_endpoint_check = ServiceEndpointCheck(name, self.context)
        self.checks.append(service_logging_check)
        self.checks.append(service_secrets_check)
        self.checks.append(service_endpoint_check)

        # Run all Checks
        super().scan()

        self.time = time.time() - start_time
