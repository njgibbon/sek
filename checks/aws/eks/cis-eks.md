# CIS - EKS
Detailed coverage examination of Sek against: CIS Benchmarks - Kubernetes - EKS - v1.0.1 - https://learn.cisecurity.org/benchmarks


# 1 - Control Plane Components
No actionable controls.


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
Judgement based on the overarching RBAC model and use of K8s and AWS in the organisation on who should be able to administer a cluster.
### 4.1.2 - Minimize access to secrets
In-cluster - A judgement based on workloads and other entities having only access to what they require to perform their Role.
### 4.1.3 Minimize wildcard use in Roles and ClusterRoles
In-cluster - Somewhat automatable. Can find all exceptions but sometimes wildcard usage may be semantically correct.
### 4.1.4 Minimize access to create pods
In-cluster - A judgement based on a secure and sensible overarching RBAC model.
### 4.1.5 Ensure that default service accounts are not actively used
In-cluster - Fully automatable.
### 4.1.6 Ensure that Service Account Tokens are only mounted where necessary
In-cluster - Fully automatable. Check all service accounts have the correct none automount setting. However, it still does not verify that all workloads have the correct minimal permission set they require.
## 4.2 - Pod Security Policies
In-cluster - Somewhat automatable. You can scan for compliance with all of the below. But sometimes these features are required. Also, it is solution-dependent in how these policies and exceptions are being managed.
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
In-cluster - Solution-dependent. The criteria here appears to be around ensuring Network Policy enforcement is implemented.
### 4.3.2 Ensure that all Namespaces have Network Policies defined
In-cluster - Fully automatable. Check each namespace for one or more network policies. This does not ensure they follow a good model or the right level of granularity.
## 4.4 - Secrets Management
### 4.4.1 Prefer using secrets as files over secrets as environment variables
In-cluster - Fully automatable. Can scan for any pods which consume a K8s Secret as an environment variable.
### 4.4.2 Consider external secret storage
Solution-dependent.
## 4.5 - Extensible Admission Control
No actionable controls.
## 4.6 - General Policies
### 4.6.1 Create administrative boundaries between resources using namespaces
In-cluster - Fully automatable. Check namespaces exist. You would still need to judge that namespacing, tenancy and workloads follow some sensible model.
### 4.6.2 Apply Security Context to Your Pods and Containers
In-cluster - Somewhat automatable. Same as all 'Pod Security Policy' controls.
### 4.6.3 The default namespace should not be used
In-cluster - Fully automatable. Ensure no resources exist in the default namespace.


# 5 - Managed services
## 5.1 Image Registry and Image Scanning
### 5.1.1 Ensure Image Vulnerability Scanning using Amazon ECR image scanning or a third party provider
Depends on Image scanning solution.
### 5.1.2 Minimize user access to Amazon ECR
Requires a detailed RBAC analysis which is context dependent. It depends on the organisation and how they are using AWS in the whole.
### 5.1.3 Minimize cluster access to read-only for Amazon ECR
Covered by Sek.
### 5.1.4 Minimize Container Registries to only those approved
Solution-dependent. Can be done with policy-based admission controllers, network policies, firewalls, proxy policies, network architecture etc.
## 5.2 Identity and Access Management (IAM)
### 5.2.1 Prefer using dedicated EKS Service Accounts
Covered by Sek.
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
In-cluster. Somewhat automatable. Looks for Network Policies. You still need to ensure a network plugin supports the policies. And you still need to judge if the model is good.
### 5.4.5 Encrypt traffic to HTTPS load balancers with TLS certificates
Solution-dependent.
## 5.5 - Authentication and Authorization
### 5.5.1 Manage Kubernetes RBAC users with AWS IAM Authenticator for Kubernetes
In-cluster - Fully automatable. Analyse aws-auth ConfigMap contents. But it still will not fully verify a sensible AWS to K8s RBAC model.
## 5.6 - Other Cluster Configurations
### 5.6.1 Consider Fargate for running untrusted workloads
Solution-dependent.


# Resources
* Sek AWS EKS Checks - [readme.md](readme.md)
* Kube Bench for EKS
    * https://github.com/aquasecurity/kube-bench/tree/main/cfg/eks-1.0
    * https://github.com/aquasecurity/kube-bench/blob/main/job-eks.yaml
