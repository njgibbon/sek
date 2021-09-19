import sys
import inspect
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

        # Register all AWS EKS Checks
        for check_class in CoreCheck.__subclasses__():
            self.checks.append(check_class(name, self.context))

        # Run all Checks
        super().scan()

        self.time = time.time() - start_time
