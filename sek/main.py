import argparse
import sys

from .aws.eks.runner import AWSEKSRunner


def main():
    cloud_choices = ['aws']
    resource_choices = ['eks']

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--version', '-version', '--v', '-v', action='version', version='0.0.14')
    arg_parser.add_argument('--cloud', action='store', type=str, required=True, choices=cloud_choices, help='Target Cloud Provider.')
    arg_parser.add_argument('--resource', action='store', type=str, required=True, choices=resource_choices, help='Target Cloud Resource.')
    arg_parser.add_argument('--name', action='store', type=str, required=True, help='Target Cloud Resource Name.')
    args = arg_parser.parse_args()

    CLOUD = args.cloud
    RESOURCE = args.resource
    NAME = args.name

    print("Sek - Live Cloud Resource Security Configuration Scanning\n-----")
    print("Cloud: " + CLOUD + " - Resource: " + RESOURCE + " - Name: " + NAME + "\n-----")
    print("Scan\n-----")

    runner = run(CLOUD, RESOURCE, NAME)

    if runner is False:
        print("No Cloud / Resource match. See: https://github.com/njgibbon/sek/blob/main/checks/readme.md")
        sys.exit(1)

    print(runner.format_results(), end="")
    print("-----")
    print("Check Document: " + runner.link)
    print("-----")
    print("Stats")
    print("-----")
    print(runner.format_stats())

    stats = runner.stats()
    if stats["checks"] != stats["passed"]:
        sys.exit(1)


def run(cloud, resource, name):
    if cloud == "aws" and resource == "eks":
        runner = AWSEKSRunner(name)
        return runner
    else:
        return False


if __name__ == '__main__':
    main()
