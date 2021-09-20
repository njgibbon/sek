import boto3


class AWSEKSContext():
    def __init__(self, name):
        # SDK Clients
        self.eks_client = boto3.client("eks")
        self.ec2_client = boto3.client("ec2")

        # EKS Info
        self.cluster_description = self.eks_client.describe_cluster(name=name)

        # Security Groups
        service_security_group_ids = []
        cluster_security_group_id = self.cluster_description["cluster"]["resourcesVpcConfig"]["clusterSecurityGroupId"]
        addtional_security_group_ids = self.cluster_description["cluster"]["resourcesVpcConfig"]["securityGroupIds"]
        service_security_group_ids.append(cluster_security_group_id)
        for sg_id in addtional_security_group_ids:
            service_security_group_ids.append(sg_id)
        self.service_security_groups = self.ec2_client.describe_security_groups(GroupIds=service_security_group_ids)
