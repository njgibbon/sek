import time

from ...core.runner import CoreRunner
from .context import AWSEKSContext
from .checks import *  # noqa


class AWSEKSRunner(CoreRunner):
    def __init__(self, name):
        start_time = time.time()
        super().__init__(name)
        self.link = "https://github.com/njgibbon/sek/blob/main/checks/aws/eks/readme.md"
        self.context = AWSEKSContext(name)
        for check_class in CoreCheck.__subclasses__():  # noqa
            self.checks.append(check_class(name, self.context))
        super().scan()
        self.time = time.time() - start_time
