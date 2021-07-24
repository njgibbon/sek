import boto3

from ...core_context import CoreContext


class AWSEKSContext(CoreContext):
    eks_client = boto3.client("eks")
    ec2_client = boto3.client("ec2")

    def __init__(self, name):
        super().__init__(name)
        self.cloud = "aws"
        self.resource = "eks"
        self.new = "new"
        self.frog = "bababa"
        # self.cluster_description = self.eks_client.describe_cluster(name=name)

