# CIS - EKS
Detailed coverage examination of Sek against: CIS Benchmarks - Kubernetes - EKS - v1.0.1 - https://learn.cisecurity.org/benchmarks


# 1 - Control Plane Components
No actionable checks.


# 2 - Control Plane Configuration
All defined Checks in this section are covered by Sek.
## 2.1 - Logging
### 2.1.1 - Enable audit Logs


# 3 - Worker Nodes
All defined Checks in this section are covered by Kube-Bench.
## 3.1 - Worker Node Configuration Files
### 3.1.1 Ensure that the kubeconfig file permissions are set to 644 or more restrictive
### 3.1.2 Ensure that the kubelet kubeconfig file ownership is set to root:root
### 3.1.3 Ensure that the kubelet configuration file has permissions set to 644 or more restrictive
### 3.1.4 Ensure that the kubelet configuration file ownership is set to root:root
## 3.2 - Kubelet
### 3.2.1 Ensure that the --anonymous-auth argument is set to false
### 3.2.2 Ensure that the --authorization-mode argument is not set to AlwaysAllow
### 3.2.3 Ensure that the --client-ca-file argument is set as appropriate
### 3.2.4 Ensure that the --read-only-port is secured
### 3.2.5 Ensure that the --streaming-connection-idle-timeout argument is not set to 0
### 3.2.6 Ensure that the --protect-kernel-defaults argument is set to true
### 3.2.7 Ensure that the --make-iptables-util-chains argument is set to true
### 3.2.8 Ensure that the --hostname-override argument is not set
### 3.2.9 Ensure that the --eventRecordQPS argument is set to 0 or a level which ensures appropriate event capture
### 3.2.10 Ensure that the --rotate-certificates argument is not set to false
### 3.2.11 Ensure that the RotateKubeletServerCertificate argument is set to true


# 4 - Policies
## 4.1 - RBAC and Service Accounts
## 4.2 - Pod Security Policies
## 4.3 - CNI Plugin
## 4.4 - Secrets Management
## 4.5 - Extensible Admission Control
## 4.6 - General Policies


# 5 - Managed services
## 5.1 Image Registry and Image Scanning
## 5.2 Identity and Access Management (IAM)
## 5.3 AWS Key Management Service (KMS)
## 5.4 - Cluster Networking
## 5.5 - Authentication and Authorization
## 5.6 - Other Cluster Configurations


# Resources
* Sek AWS EKS Checks - [readme.md](readme.md)
* Kube Bench for EKS
    * https://github.com/aquasecurity/kube-bench/tree/main/cfg/eks-1.0
    * https://github.com/aquasecurity/kube-bench/blob/main/job-eks.yaml
