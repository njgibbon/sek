from ...runner import Runner as CoreRunner
from .context import Context
from .checks.check import Check
class Runner(CoreRunner):
    def __init__(self, cloud, resource, name):
        print("EKS Runner")
        super().__init__(cloud, resource, name)
        self.context = Context()
        check = Check(self.context)
        self.checks.append(check)
        self.time = None
        super().scan()
