from ...check import Check as CoreCheck
class Check(CoreCheck): 
    def __init__(self, context):
        print("EKS Check")
        super().__init__(context)
        self.cloud = "aws"
        self.resource = "eks"

