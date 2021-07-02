"""
SEK - Runtime Cloud Security and Misconfiguration Scanning.
AWS - EKS - Nodes.
"""
import unittest
import os
import boto3
import warnings

cluster_name = os.getenv("SEK_AWS_EKS_CLUSTER_NAME")

eks_node_filter = [{
    "Name": "tag:kubernetes.io/cluster/" + cluster_name,
    "Values": ["owned"]
}]
ec2_client = boto3.client("ec2")
eks_nodes = ec2_client.describe_instances(Filters=eks_node_filter)


class TestAWSEKSNodes(unittest.TestCase):

    def test_imds(self):
        print("AWS - EKS - Nodes - IMDS")
        global eks_nodes
        for node in eks_nodes["Reservations"]:
            metadata_options = node["Instances"][0]["MetadataOptions"]
            if metadata_options['HttpEndpoint'] is False:
                continue
            else:
                if metadata_options["HttpTokens"] != "required":
                    assert False

    def test_unrestricted_security_groups_ingress(self):
        print("AWS - EKS - Nodes - Security Groups")
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>")
        global eks_nodes
        global ec2_client
        security_group_ids = []
        for node in eks_nodes["Reservations"]:
            security_groups = node["Instances"][0]["SecurityGroups"]
            for sg in security_groups:
                security_group_ids.append(sg["GroupId"])
        if security_group_ids != []:
            security_groups = ec2_client.describe_security_groups(GroupIds=security_group_ids)
            for sg in security_groups["SecurityGroups"]:
                for ip in sg["IpPermissions"]:
                    any_protocol = False
                    any_port = False
                    any_range = False
                    # Protocol
                    if 'FromPort' not in ip.keys():
                        any_protocol = True
                    # Port
                    if ip["IpProtocol"] == "-1":
                        any_port = True
                    # Range
                    for ipv4_range in ip["IpRanges"]:
                        if ipv4_range["CidrIp"] == "0.0.0.0/0":
                            any_range = True
                    if any_protocol and any_port and any_range:
                        assert False

    def test_volume_encryption(self):
        print("AWS - EKS - Nodes - Volume Encryption")
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>")
        global eks_nodes
        ec2_resource = boto3.resource("ec2")
        for node in eks_nodes["Reservations"]:
            devices = node["Instances"][0]["BlockDeviceMappings"]
            for device in devices:
                volume = ec2_resource.Volume(device["Ebs"]["VolumeId"])
                assert volume.encrypted is True

    def test_private_subnets(self):
        print("AWS - EKS - Nodes - Private Subnets")
        global eks_nodes
        global ec2_client
        subnet_ids = []
        # Obtain Node Subnet IDs
        for node in eks_nodes["Reservations"]:
            subnet_id = node["Instances"][0]["SubnetId"]
            if subnet_id not in subnet_ids:
                subnet_ids.append(subnet_id)
        # Obtain Route Tables associated to Subnets
        if subnet_ids != []:
            route_table_filter = [{
                "Name": "association.subnet-id",
                "Values": subnet_ids
            }]
            route_tables = ec2_client.describe_route_tables(Filters=route_table_filter)
            # Check if there are any Public Subnets
            for rt in route_tables["RouteTables"]:
                for r in rt["Routes"]:
                    if "DestinationCidrBlock" in r and "GatewayId" in r:
                        if r["DestinationCidrBlock"] == "0.0.0.0/0" and "igw-" in r["GatewayId"]:
                            assert False

    def test_no_public_ip_dns(self):
        print("AWS - EKS - Nodes - No Public IP or DNS")
        global eks_nodes
        for node in eks_nodes["Reservations"]:
            public_dns_name = node["Instances"][0]["PublicDnsName"]
            public_ip = node["Instances"][0]["PublicIpAddress"]
            if public_dns_name != "" or public_ip != "":
                assert False


if __name__ == "__main__":
    unittest.main()
