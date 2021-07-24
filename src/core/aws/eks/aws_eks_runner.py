from ...core_runner import CoreRunner
from .aws_eks_context import AWSEKSContext
from .checks.abc_aws_eks_check import ABCAWSEKSCheck


class AWSEKSRunner(CoreRunner):
    def __init__(self, name):
        print("EKS Runner")
        super().__init__(name)
        self.cloud = "aws"
        self.resource = "eks"
        self.context = AWSEKSContext(name)
        abc = ABCAWSEKSCheck(name, self.context)
        self.checks.append(abc)
        self.time = None
        super().scan()
