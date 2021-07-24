from ..aws_eks_check import AWSEKSCheck


class ABCAWSEKSCheck(AWSEKSCheck): 
    def __init__(self, resource_name, context):
        print("ABC EKS Check")
        super().__init__(resource_name, context)

    def scan(self):
        print(self.context.new)
        print(self.context.frog)
        print(self.resource_name)
