import boto3

from ...core.core_context import CoreContext


class AWSEKSContext(CoreContext):
    def __init__(self, name):
        super().__init__(name)
        self.cloud = "aws"
        self.resource = "eks"
        self.eks_client = boto3.client("eks")
        self.ec2_client = boto3.client("ec2")
        self.cluster_description = self.eks_client.describe_cluster(name=name)
