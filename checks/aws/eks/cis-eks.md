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
### 4.1.1 Ensure that the cluster-admin role is only used where required
### 4.1.2 - Minimize access to secrets
### 4.1.3 Minimize wildcard use in Roles and ClusterRoles
### 4.1.4 Minimize access to create pods
### 4.1.5 Ensure that default service accounts are not actively used
### 4.1.6 Ensure that Service Account Tokens are only mounted where necessary
## 4.2 - Pod Security Policies
### 4.2.1 Minimize the admission of privileged containers
### 4.2.2 Minimize the admission of containers wishing to share the host process ID namespace
### 4.2.3 Minimize the admission of containers wishing to share the host IPC namespace
### 4.2.4 Minimize the admission of containers wishing to share the host network namespace
### 4.2.5 Minimize the admission of containers with allowPrivilegeEscalation
### 4.2.6 Minimize the admission of root containers
### 4.2.7 Minimize the admission of containers with the NET_RAW capability
### 4.2.8 Minimize the admission of containers with added capabilities
### 4.2.9 Minimize the admission of containers with capabilities assigned
## 4.3 - CNI Plugin
### 4.3.1 Ensure latest CNI version is used
### 4.3.2 Ensure that all Namespaces have Network Policies defined
## 4.4 - Secrets Management
### 4.4.1 Prefer using secrets as files over secrets as environment variables
### 4.4.2 Consider external secret storage
## 4.5 - Extensible Admission Control
## 4.6 - General Policies
### 4.6.1 Create administrative boundaries between resources using namespaces
### 4.6.2 Apply Security Context to Your Pods and Containers
### 4.6.3 The default namespace should not be used


# 5 - Managed services
## 5.1 Image Registry and Image Scanning
### 5.1.1 Ensure Image Vulnerability Scanning using Amazon ECR image scanning or a third party provider
Depends on Image scanning solution.
### 5.1.2 Minimize user access to Amazon ECR
Requires a detailed RBAC analysis which is context dependent. It depends on the organisation and how they are using AWS in the whole.
### 5.1.3 Minimize cluster access to read-only for Amazon ECR
Covered by Sek.
### 5.1.4 Minimize Container Registries to only those approved
Depends on Solution. Can be done with policy-based admission controllers, network policies, firewalls, proxy policies, network architecture etc.
## 5.2 Identity and Access Management (IAM)
### 5.2.1 Prefer using dedicated EKS Service Accounts
## 5.3 AWS Key Management Service (KMS)
### 5.3.1 Ensure Kubernetes Secrets are encrypted using Customer Master Keys (CMKs) managed in AWS KMS
Covered by Sek.
## 5.4 - Cluster Networking
### 5.4.1 Restrict Access to the Control Plane Endpoint
Covered by Sek.
### 5.4.2 Ensure clusters are created with Private Endpoint Enabled and Public Access Disabled
Covered by Sek.
### 5.4.3 Ensure clusters are created with Private Nodes
Covered by Sek.
### 5.4.4 Ensure Network Policy is Enabled and set as appropriate
### 5.4.5 Encrypt traffic to HTTPS load balancers with TLS certificates
## 5.5 - Authentication and Authorization
### 5.5.1 Manage Kubernetes RBAC users with AWS IAM Authenticator for Kubernetes
## 5.6 - Other Cluster Configurations
### 5.6.1 Consider Fargate for running untrusted workloads


# Resources
* Sek AWS EKS Checks - [readme.md](readme.md)
* Kube Bench for EKS
    * https://github.com/aquasecurity/kube-bench/tree/main/cfg/eks-1.0
    * https://github.com/aquasecurity/kube-bench/blob/main/job-eks.yaml
