import argparse
import os

from core.aws.eks.aws_eks_runner import AWSEKSRunner


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--cloud', action='store', type=str, required=True)
    arg_parser.add_argument('--resource', action='store', type=str, required=True)
    arg_parser.add_argument('--name', action='store', type=str, required=True)
    args = arg_parser.parse_args()

    CLOUD = args.cloud
    RESOURCE = args.resource
    NAME = args.name

    core(CLOUD, RESOURCE, NAME)


def core(cloud, resource, name):
    if cloud == "aws" or cloud == "AWS" and resource == "eks" or resource == "EKS":
        aws_eks_runner = AWSEKSRunner(name)


if __name__ == '__main__':
    main()
