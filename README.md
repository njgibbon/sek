![sek](images/sek.png)
Runtime Cloud Security and Misconfiguration Scanning.

First focus on AWS - EKS. SEK - EKS - SEK. Get it?

# scripts
Concept / MVP logic.

1. Clone this project and move to the top-level directory.
```
cd scripts
```
2. Configure AWS Permissions: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
3. Configure the tool.
```
export SEK_AWS_EKS_CLUSTER_NAME=<aws-eks-cluster-name>
```
4. Run Checks.
```
# EKS Checks
python3 test_aws_eks.py
```
