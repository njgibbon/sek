from ..check import Check as EKSCheck
class Check(EKSCheck): 
    def __init__(self, context):
        print("EKS Check - Actual")
        super().__init__(context)

    def scan(self):
        print(self.context.new)
