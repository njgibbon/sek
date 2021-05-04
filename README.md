# Sek

# MVP 0
* Clone this project and move to the top-level directory.
* Move to the MVP directory.
```
cd py/mvp-0
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
