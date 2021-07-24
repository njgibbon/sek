import time

from ...core_runner import CoreRunner
from .aws_eks_context import AWSEKSContext
from .checks.abc_aws_eks_check import ABCAWSEKSCheck


class AWSEKSRunner(CoreRunner):
    def __init__(self, name):
        start_time = time.time()
        super().__init__(name)
        self.cloud = "aws"
        self.resource = "eks"
        self.link = "https://github.com/njgibbon/sek/blob/main/checks/aws/eks"
        self.context = AWSEKSContext(name)
        abc = ABCAWSEKSCheck(name, self.context)
        self.checks.append(abc)
        super().scan()
        time.sleep(3)
        self.time = time.time() - start_time
