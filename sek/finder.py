from .core.aws.eks.aws_eks_runner import AWSEKSRunner


def finder(cloud, resource, name):
    if ( cloud == "aws" or cloud == "AWS" ) and ( resource == "eks" or resource == "EKS" ):
        runner = AWSEKSRunner(name)
        return runner
    else:
        return False
