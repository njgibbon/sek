from ...core_context import CoreContext


class AWSEKSContext(CoreContext): 
    def __init__(self, name):
        print("EKS Context")
        super().__init__(name)
        self.cloud = "aws"
        self.resource = "eks"
        self.new = "new"
        self.frog = "bababa"

