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
export SEK_EKS_CLUSTER_NAME=<eks-cluster-name>
```
* Run Checks.
```
# All Checks
python3 -m unittest

# Managed Service Checks
python3 test_eks_managed_service.py

# Node Checks
python3 test_eks_nodes.py
```
