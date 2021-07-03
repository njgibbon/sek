# Sek
Runtime Cloud Security and Misconfiguration Scanning.

# scripts
* Clone this project and move to the top-level directory.
```
cd scripts
```
* Configure AWS Permissions: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
* Configure the tool.
```
export SEK_AWS_EKS_CLUSTER_NAME=<aws-eks-cluster-name>
```
* Run Checks.
```
# All Checks
python3 -m unittest

# EKS Checks
python3 test_aws_eks.py
```
