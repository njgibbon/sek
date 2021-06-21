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

# Control Plane Checks
python3 test_eks_control_plane.py

# Node Checks
python3 test_eks_nodes.py
```
