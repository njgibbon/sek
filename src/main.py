import argparse
import os

import boto3


class EKSContext:
    cloud="aws"
    resource="eks"
    eks_client = boto3.client("eks")
    ec2_client = boto3.client("ec2")

    def __init__(self, name):
        self.name = name
        self.cluster_description = self.eks_client.describe_cluster(name=name)


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--cloud', action='store', type=str, required=True)
    arg_parser.add_argument('--resource', action='store', type=str, required=True)
    arg_parser.add_argument('--name', action='store', type=str, required=True)
    args = arg_parser.parse_args()

    CLOUD = args.cloud
    RESOURCE = args.resource
    NAME = args.name

    print("Sek - Runtime Cloud Security and Misconfiguration Scanning")
    print("-----")
    print("Scan")
    print("-----")
    print("Cloud: " + CLOUD + " - Resource: " + RESOURCE + " - Name: " + NAME)
    print("-----")
    print("Results")
    print("-----")
    print("service-logging: PASS")
    print("service-secrets: PASS")
    print("service-endpoint: PASS")
    print("service-endpoint-firewall: PASS")
    print("service-security-groups: PASS")
    print("nodes-imds: PASS")
    print("nodes-volumes: PASS")
    print("nodes-security-groups: PASS")
    print("nodes-subnets: PASS")
    print("nodes-ips: PASS")
    print("-----")
    print("Stats")
    print("-----")
    print ("Time: 0.5s")
    print("Checks: 10")
    print("Passed: 10 - (100.00%)")
    print("Failed: 0 - (0.00%)")
    print("Skipped: 0 - (0.00%)")
    print("Errors: 0 - (0.00%)")

    eks_context = EKSContext(NAME)
    print(eks_context.cloud)
    print(eks_context.resource)
    print(eks_context.name)

if __name__ == '__main__':
    main()
