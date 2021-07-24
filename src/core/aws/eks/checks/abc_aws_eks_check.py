from ..aws_eks_check import AWSEKSCheck
class ABCAWSEKSCheck(AWSEKSCheck): 
    def __init__(self, context):
        print("EKS Check - Actual")
        super().__init__(context)

    def scan(self):
        print(self.context.new)
