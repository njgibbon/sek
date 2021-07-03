"""
SEK - Runtime Cloud Security and Misconfiguration Scanning.
AWS - EKS.
"""
import unittest
import os
import warnings
import boto3


# Config
CLUSTER_NAME = os.getenv("SEK_AWS_EKS_CLUSTER_NAME")

# Service
EKS_CLIENT = boto3.client("eks")
EC2_CLIENT = boto3.client("ec2")
CLUSTER_DESCRIPTION = EKS_CLIENT.describe_cluster(name=CLUSTER_NAME)

CLUSTER_SECURITY_GROUP_ID = CLUSTER_DESCRIPTION["cluster"]["resourcesVpcConfig"]["clusterSecurityGroupId"]
ADDITIONAL_SECURITY_GROUP_IDS = CLUSTER_DESCRIPTION["cluster"]["resourcesVpcConfig"]["securityGroupIds"]
service_security_group_ids = []
service_security_group_ids.append(CLUSTER_SECURITY_GROUP_ID)
for sg_id in ADDITIONAL_SECURITY_GROUP_IDS:
    service_security_group_ids.append(sg_id)
SERVICE_SECURITY_GROUPS = EC2_CLIENT.describe_security_groups(GroupIds=service_security_group_ids)

# Nodes
EKS_NODE_FILTER = [{
    "Name": "tag:kubernetes.io/cluster/" + CLUSTER_NAME,
    "Values": ["owned"]
}]
EKS_NODES = EC2_CLIENT.describe_instances(Filters=EKS_NODE_FILTER)
node_security_group_ids = []
for node in EKS_NODES["Reservations"]:
    n_sgs = node["Instances"][0]["SecurityGroups"]
    for n_sg in n_sgs:
        node_security_group_ids = [].append(n_sg["GroupId"])
NODE_SECURITY_GROUPS = EC2_CLIENT.describe_security_groups(GroupIds=node_security_group_ids)


class TestAWSEKS(unittest.TestCase):
    """AWS - EKS"""
    print("AWS - EKS")

    # Service Checks
    def test_service_endpoint_access(self):
        """AWS - EKS - Service - Endpoint Access"""
        print("AWS - EKS - Service - Endpoint Access")
        global CLUSTER_DESCRIPTION  # pylint: disable=global-statement
        self.assertFalse(CLUSTER_DESCRIPTION["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"])
        self.assertTrue(CLUSTER_DESCRIPTION["cluster"]["resourcesVpcConfig"]["endpointPrivateAccess"])

    def test_service_control_plane_logging(self):
        """AWS - EKS - Service - Logging"""
        print("AWS - EKS - Service - Logging")
        global CLUSTER_DESCRIPTION  # pylint: disable=global-statement
        log_types = ["audit", "api", "authenticator", "controllerManager", "scheduler"]
        all_log_types_found = False
        if all(item in CLUSTER_DESCRIPTION["cluster"]["logging"]["clusterLogging"][0]["types"] for item in log_types):
            all_log_types_found = True
        self.assertTrue(all_log_types_found)

    def test_service_envelope_encryption_for_secrets(self):
        """AWS - EKS - Service - Secret Encryption"""
        print("AWS - EKS - Service - Secret Encryption")
        global CLUSTER_DESCRIPTION  # pylint: disable=global-statement
        envelope_encryption_config_found = False
        for item in CLUSTER_DESCRIPTION["cluster"]["encryptionConfig"][0]["resources"]:
            if item == "secrets":
                envelope_encryption_config_found = True
        self.assertTrue(envelope_encryption_config_found)

    def test_service_unrestricted_public_endpoint_access_if_enabled(self):
        """AWS - EKS - Service - Public Endpoint Restriction"""
        print("AWS - EKS - Service - Public Endpoint Restriction")
        global CLUSTER_DESCRIPTION  # pylint: disable=global-statement
        if CLUSTER_DESCRIPTION["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"] is True:
            for ipv4_range in CLUSTER_DESCRIPTION["cluster"]["resourcesVpcConfig"]["publicAccessCidrs"]:
                self.assertFalse(ipv4_range == "0.0.0.0/0")

    def test_service_unrestricted_security_groups_ingress(self):
        """AWS - EKS - Service - Security Groups"""
        print("AWS - EKS - Service - Security Groups")
        global SERVICE_SECURITY_GROUPS  # pylint: disable=global-statement
        result = self.unrestricted_security_groups_ingress(SERVICE_SECURITY_GROUPS)
        self.assertFalse(result)

    # Node Checks
    def test_nodes_imds(self):
        """AWS - EKS - Nodes - IMDS"""
        print("AWS - EKS - Nodes - IMDS")
        global EKS_NODES  # pylint: disable=global-statement
        for n in EKS_NODES["Reservations"]:
            metadata_options = n["Instances"][0]["MetadataOptions"]
            if metadata_options['HttpEndpoint'] is True:
                self.assertFalse(metadata_options["HttpTokens"] != "required")

    def test_nodes_unrestricted_security_groups_ingress(self):
        """AWS - EKS - Nodes - Security Groups"""
        print("AWS - EKS - Nodes - Security Groups")
        global NODE_SECURITY_GROUPS  # pylint: disable=global-statement
        result = self.unrestricted_security_groups_ingress(NODE_SECURITY_GROUPS)
        self.assertFalse(result)

    def test_nodes_volume_encryption(self):
        """AWS - EKS - Nodes - Volume Encryption"""
        print("AWS - EKS - Nodes - Volume Encryption")
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>")
        global EKS_NODES  # pylint: disable=global-statement
        ec2_resource = boto3.resource("ec2")
        for n in EKS_NODES["Reservations"]:
            devices = n["Instances"][0]["BlockDeviceMappings"]
            for device in devices:
                volume = ec2_resource.Volume(device["Ebs"]["VolumeId"])
                self.assertTrue(volume.encrypted)

    def test_nodes_private_subnets(self):
        """AWS - EKS - Nodes - Private Subnets"""
        print("AWS - EKS - Nodes - Private Subnets")
        global EKS_NODES  # pylint: disable=global-statement
        global EC2_CLIENT  # pylint: disable=global-statement
        subnet_ids = []
        # Obtain Node Subnet IDs
        for n in EKS_NODES["Reservations"]:
            subnet_id = n["Instances"][0]["SubnetId"]
            if subnet_id not in subnet_ids:
                subnet_ids.append(subnet_id)
        # Obtain Route Tables associated to Subnets
        if subnet_ids != []:
            route_table_filter = [{
                "Name": "association.subnet-id",
                "Values": subnet_ids
            }]
            route_tables = EC2_CLIENT.describe_route_tables(Filters=route_table_filter)
            # Check if there are any Public Subnets
            for rt in route_tables["RouteTables"]:
                for r in rt["Routes"]:
                    if "DestinationCidrBlock" in r and "GatewayId" in r:
                        self.assertFalse(r["DestinationCidrBlock"] == "0.0.0.0/0" and "igw-" in r["GatewayId"])

    def test_nodes_no_public_ip_dns(self):
        """AWS - EKS - Nodes - No Public IP or DNS"""
        print("AWS - EKS - Nodes - No Public IP or DNS")
        global EKS_NODES  # pylint: disable=global-statement
        for n in EKS_NODES["Reservations"]:
            public_dns_name = n["Instances"][0]["PublicDnsName"]
            public_ip = n["Instances"][0]["PublicIpAddress"]
            self.assertFalse(public_dns_name != "" or public_ip != "")

    # Helpers
    def unrestricted_security_groups_ingress(self, sgs):  # pylint: disable=no-self-use
        """If Protocol, Ports and Range conjunction is *"""
        for sg in sgs["SecurityGroups"]:
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
                    return True
        return False


if __name__ == "__main__":
    unittest.main()
