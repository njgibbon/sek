# CIS


# 1 - Control Plane Components
No actionable checks.
# 2 - Control Plane Configuration
## 2.1 - Logging
All defined Logging Checks covered by Sek.
### 2.1.1 - Enable audit Logs
# 3 - Worker Nodes
All defined Node Checks covered by Kube-Bench for EKS.
## 3.1 - Worker Node Configuration Files
### 3.1.1 Ensure that the kubeconfig file permissions are set to 644 or more restrictive
### 3.1.2 Ensure that the kubelet kubeconfig file ownership is set to root:root
### 3.1.3 Ensure that the kubelet configuration file has permissions set to 644 or more restrictive
### 3.1.4 Ensure that the kubelet configuration file ownership is set to root:root
## 3.2 - Kubelet
### 3.2.1 Ensure that the --anonymous-auth argument is set to false
# 4 - Policies
# 5 - Managed services

# Resources
* Sek AWS EKS Checks - [readme.md](readme.md)
* Kube Bench for EKS
    * https://github.com/aquasecurity/kube-bench/tree/main/cfg/eks-1.0
    * https://github.com/aquasecurity/kube-bench/blob/main/job-eks.yaml
