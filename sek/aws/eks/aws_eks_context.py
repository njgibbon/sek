import boto3

class AWSEKSContext():
    def __init__(self, name):
        self.eks_client = boto3.client("eks")
        self.ec2_client = boto3.client("ec2")
        self.cluster_description = self.eks_client.describe_cluster(name=name)
