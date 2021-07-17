# Scripts
Concept / MVP logic.

1. Clone this project and move to the `scripts` directory.
```
git clone https://github.com/njgibbon/sek.git
cd sek/scripts
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
