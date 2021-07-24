from ...core_runner import CoreRunner
from .aws_eks_context import AWSEKSContext
from .checks.abc_aws_eks_check import ABCAWSEKSCheck
class AWSEKSRunner(CoreRunner):
    def __init__(self, cloud, resource, name):
        print("EKS Runner")
        super().__init__(cloud, resource, name)
        self.context = AWSEKSContext()
        abc = ABCAWSEKSCheck(self.context)
        self.checks.append(abc)
        self.time = None
        super().scan()
