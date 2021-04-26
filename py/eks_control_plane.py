"""
AWS - EKS - Control Plane - Runtime Security and Misconfiguration Scanning
"""
import unittest
import os
import boto3

cluster_name = os.getenv('SEK_CLUSTER_NAME')
 
eks_client = boto3.client('eks')
cluster_description = eks_client.describe_cluster(name=cluster_name)

cluster_security_group_id = cluster_description["cluster"]["resourcesVpcConfig"]["clusterSecurityGroupId"]
additional_security_group_ids = cluster_description["cluster"]["resourcesVpcConfig"]["securityGroupIds"]
security_group_ids = []
security_group_ids.append(cluster_security_group_id)
for id in additional_security_group_ids:
    security_group_ids.append(id)
ec2_client = boto3.client('ec2')
security_groups = ec2_client.describe_security_groups(GroupIds=security_group_ids)

class EKSControlPlane(unittest.TestCase):

    def test_endpoint_access(self):
        global cluster_description
        assert cluster_description["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"] is False
        assert cluster_description["cluster"]["resourcesVpcConfig"]["endpointPrivateAccess"] is True
        
    def test_control_plane_logging(self):
        global cluster_description
        log_types = ["audit", "api", "authenticator", "controllerManager", "scheduler"]
        all_log_types_found = False
        if all (item in cluster_description["cluster"]["logging"]["clusterLogging"][0]["types"] for item in log_types):
            all_log_types_found = True
        assert all_log_types_found is True

    def test_envelope_encryption_for_secrets(self):
        global cluster_description
        envelope_encryption_config_found = False
        for item in cluster_description["cluster"]["encryptionConfig"][0]["resources"]:
            if item == "secrets":
                envelope_encryption_config_found = True
        assert envelope_encryption_config_found is True

    def test_endpoint_https(self):
        global cluster_description
        https_found = False
        if "https" in cluster_description["cluster"]["endpoint"]:
            https_found = True
        assert https_found is True
    
    def test_unrestricted_public_endpoint_access_if_enabled(self):
        global cluster_description
        if cluster_description["cluster"]["resourcesVpcConfig"]["endpointPublicAccess"] is True:
            for ipv4_range in cluster_description["cluster"]["resourcesVpcConfig"]["publicAccessCidrs"]:
                if ipv4_range == "0.0.0.0/0":
                    assert False

    def test_unrestricted_security_groups_ingress(self):
        # If Protocol, Ports and Range conjunction is *
        global security_groups
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

if __name__ == '__main__':
    unittest.main()
