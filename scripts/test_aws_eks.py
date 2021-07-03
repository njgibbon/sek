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
for id in ADDITIONAL_SECURITY_GROUP_IDS:
    service_security_group_ids.append(id)
SERVICE_SECURITY_GROUPS = EC2_CLIENT.describe_SECURITY_GROUPS(GroupIds=service_security_group_ids)

# Nodes
EKS_NODE_FILTER = [{
    "Name": "tag:kubernetes.io/cluster/" + CLUSTER_NAME,
    "Values": ["owned"]
}]
EKS_NODES = EC2_CLIENT.describe_instances(Filters=EKS_NODE_FILTER)
node_security_group_ids = []
for node in EKS_NODES["Reservations"]:
    n_sgs = node["Instances"][0]["SecurityGroups"]
    for sg in n_sgs:
        node_security_group_ids = [].append(sg["GroupId"])
NODE_SECURITY_GROUPS = EC2_CLIENT.describe_security_groups(GroupIds=node_security_group_ids)

class TestAWSEKS(unittest.TestCase):

    # Service Checks
    def test_service_endpoint_access():
        print("AWS - EKS - Service - Endpoint Access")
        global CLUSTER_DESCRIPTION
        assert CLUSTER_DESCRIPTION["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"] is False
        assert CLUSTER_DESCRIPTION["cluster"]["resourcesVpcConfig"]["endpointPrivateAccess"] is True

    def test_service_control_plane_logging():
        print("AWS - EKS - Service - Logging")
        global CLUSTER_DESCRIPTION
        log_types = ["audit", "api", "authenticator", "controllerManager", "scheduler"]
        all_log_types_found = False
        if all(item in CLUSTER_DESCRIPTION["cluster"]["logging"]["clusterLogging"][0]["types"] for item in log_types):
            all_log_types_found = True
        assert all_log_types_found is True

    def test_service_envelope_encryption_for_secrets():
        print("AWS - EKS - Service - Secret Encryption")
        global CLUSTER_DESCRIPTION
        envelope_encryption_config_found = False
        for item in CLUSTER_DESCRIPTION["cluster"]["encryptionConfig"][0]["resources"]:
            if item == "secrets":
                envelope_encryption_config_found = True
        assert envelope_encryption_config_found is True

    def test_service_unrestricted_public_endpoint_access_if_enabled():
        print("AWS - EKS - Service - Public Endpoint Restriction")
        global CLUSTER_DESCRIPTION
        if CLUSTER_DESCRIPTION["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"] is True:
            for ipv4_range in CLUSTER_DESCRIPTION["cluster"]["resourcesVpcConfig"]["publicAccessCidrs"]:
                if ipv4_range == "0.0.0.0/0":
                    assert False

    def test_service_unrestricted_security_groups_ingress():
        print("AWS - EKS - Service - Security Groups")
        global SERVICE_SECURITY_GROUPS
        assert unrestricted_security_groups_ingress(SERVICE_SECURITY_GROUPS) is False

    # Node Checks
    def test_nodes_imds():
        print("AWS - EKS - Nodes - IMDS")
        global EKS_NODES
        for node in EKS_NODES["Reservations"]:
            metadata_options = node["Instances"][0]["MetadataOptions"]
            if metadata_options['HttpEndpoint'] is False:
                continue
            else:
                if metadata_options["HttpTokens"] != "required":
                    assert False

    def test_nodes_unrestricted_security_groups_ingress():
        print("AWS - EKS - Nodes - Security Groups")
        global NODE_SECURITY_GROUPS
        assert unrestricted_security_groups_ingress(NODE_SECURITY_GROUPS) is False

    def test_nodes_volume_encryption():
        print("AWS - EKS - Nodes - Volume Encryption")
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>")
        global EKS_NODES
        ec2_resource = boto3.resource("ec2")
        for node in EKS_NODES["Reservations"]:
            devices = node["Instances"][0]["BlockDeviceMappings"]
            for device in devices:
                volume = ec2_resource.Volume(device["Ebs"]["VolumeId"])
                assert volume.encrypted is True

    def test_nodes_private_subnets():
        print("AWS - EKS - Nodes - Private Subnets")
        global EKS_NODES
        global EC2_CLIENT
        subnet_ids = []
        # Obtain Node Subnet IDs
        for node in EKS_NODES["Reservations"]:
            subnet_id = node["Instances"][0]["SubnetId"]
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
                        if r["DestinationCidrBlock"] == "0.0.0.0/0" and "igw-" in r["GatewayId"]:
                            assert False

    def test_nodes_no_public_ip_dns():
        print("AWS - EKS - Nodes - No Public IP or DNS")
        global EKS_NODES
        for node in EKS_NODES["Reservations"]:
            public_dns_name = node["Instances"][0]["PublicDnsName"]
            public_ip = node["Instances"][0]["PublicIpAddress"]
            if public_dns_name != "" or public_ip != "":
                assert False
    
    # Helpers
    def unrestricted_security_groups_ingress(sgs):
        # If Protocol, Ports and Range conjunction is *
        for sg in sgs:
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
