from .core.aws.eks.aws_eks_runner import AWSEKSRunner

def finder(cloud, resource, name):
    if ( cloud == "aws" or cloud == "AWS" ) and ( resource == "eks" or resource == "EKS" ):
        print("Scan\n-----")
        runner = AWSEKSRunner(name)
        return runner
    else:
        print("No Cloud / Resource match. See: https://github.com/njgibbon/sek/tree/main/checks")
        sys.exit(1)
