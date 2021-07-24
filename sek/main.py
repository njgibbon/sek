import argparse
import os
import sys

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

    print("Sek - Runtime Cloud Security Scanning\n-----")
    print("Cloud: " + CLOUD + " - Resource: " + RESOURCE + " - Name: " + NAME + "\n-----")
    
    if ( CLOUD == "aws" or CLOUD == "AWS" ) and ( RESOURCE == "eks" or RESOURCE == "EKS" ):
        print("Scan\n-----")
        runner = AWSEKSRunner(NAME)
    else:
        print("No Cloud / Resource match. See: https://github.com/njgibbon/sek/tree/main/checks")
        sys.exit(1)

    print(runner.format_results(), end = "")
    print("-----")
    print("Check Document: " + runner.link)
    print("-----")
    print("Stats")
    print("-----")
    print(runner.format_stats())

    stats = runner.stats()
    if stats["checks"] != stats["passed"]:
        sys.exit(1)


if __name__ == '__main__':
    main()
