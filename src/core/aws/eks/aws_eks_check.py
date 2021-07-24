from ...core_check import CoreCheck
class AWSEKSCheck(CoreCheck): 
    def __init__(self, context):
        print("EKS Check")
        super().__init__(context)
        self.cloud = "aws"
        self.resource = "eks"

