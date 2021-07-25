# EKS Checks

## service-logging

## service-secrets
## service-endpoint
## service-endpoint-firewall
If a public EKS endpoint exists then ensure that
## service-sgs
## node-imds
## node-volumes
## node-sgs
## node-private
Also checking associated route tables for IGW routes was considered but deemed not necessary.
## node-role
Ensure that nodes only have minimal 

* Service - Logging - Audit logs. CIS EKS.
* Service - Secrets - Envelope Encryption. CIS EKS.
* Service - Private Endpoint enabled. Public Endpoint disabled. CIS EKS.
* Service - Public Endpoint Firewall if exists. CIS EKS.
* Service - Cluster SGs - No unrestricted access. ___
* Nodes - Instance Metadata Service Options. CIS EKS.
* Nodes - Encrypted Volumes. ___
* Nodes - Security Groups. ___
* Nodes - Private Subnets. _-_-
* Nodes - No Public IP or DNS Name Attached. CIS EKS.
* Nodes - Node Role minimal permissions. CIS EKS.


# Areas Not In Scope
You need to draw the line somewhere as complex services depend on and integrate with other components.

All areas identified should still be cotinuously monitored suing various tools or custom checks.

* General IAM best practises.
* In-Cluster Kubernetes Security Best Practises.
* Network Audit - VPC Flow Logs.
* Managed Service Actions Audit - CloudTrail.
* Detailed K8s audit log analysis.
* KMS Keys used for any EKS-related encryption should be rotated.
* Network architecture and VPC Endpoints.
* CIS Hardening of Nodes.
* CloudWatch Logs Encryptions with CMKs.


# Resources
* CIS Benchmarks - Kubernetes - EKS - v1.0.1 - https://learn.cisecurity.org/benchmarks
    * https://aws.amazon.com/blogs/containers/introducing-cis-amazon-eks-benchmark/
* AWS EKS Best Practises - Security - https://aws.github.io/aws-eks-best-practices/security/docs/index.html
* AWS EKS Security Documentation - https://docs.aws.amazon.com/eks/latest/userguide/security.html


# Other Resources
* Kube-Bench - https://github.com/aquasecurity/kube-bench
* CIS Benchmarks - AWS - Foundations - v1.0.4 - https://learn.cisecurity.org/benchmarks


# Scratch
2 Storage
2.2 Elastic Compute Cloud (EC2)
2.2.1 Ensure EBS volume encryption is enabled

5 Networking
5.2 Ensure no security groups allow ingress from 0.0.0.0/0 to remote server administration ports

```
* Service - Logging - Audit logs. CIS EKS.
* Service - Secrets - Envelope Encryption. CIS EKS.
* Service - Private Endpoint enabled. Public Endpoint disabled. CIS EKS.
* Service - Public Endpoint Firewall if exists. CIS EKS.
* Service - Cluster SGs - No unrestricted access. ___
* Nodes - Instance Metadata Service Options. CIS EKS.
* Nodes - Encrypted Volumes. ___
* Nodes - Security Groups. ___
* Nodes - Private Subnets. _-_-
* Nodes - No Public IP or DNS Name Attached. CIS EKS.
* Nodes - Node Role minimal permissions. CIS EKS.
```
