import argparse
import os
import sys

from .resource_finder import finder


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
    
    runner = finder(CLOUD, RESOURCE, NAME)

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
