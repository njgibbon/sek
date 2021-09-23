import time

from ...core.runner import CoreRunner
from .context import AWSEKSContext
from .checks import *  # noqa - pylint: disable=unused-wildcard-import


class AWSEKSRunner(CoreRunner):
    def __init__(self, name, skip):
        start_time = time.time()
        super().__init__(name, skip)
        self.link = "https://github.com/njgibbon/sek/blob/main/checks/aws/eks/readme.md"
        self.context = AWSEKSContext(name)
        for check_class in CoreCheck.__subclasses__():  # noqa - pylint: disable=undefined-variable
            self.checks.append(check_class(self.name, self.context, self.skip))
        super().scan()
        self.time = time.time() - start_time
