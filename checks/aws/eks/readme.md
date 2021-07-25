# EKS Checks

## service-logging
Audit logs.

## service-secrets
Envelope encryption for Kubernetes Secrets with KMS.

## service-endpoint
Private Endpoint enabled. Public Endpoint disabled.

## service-endpoint-firewall
If a public EKS endpoint exists then ensure that there is no unrestricted access.

## service-sgs
No unrestricted access.

* CIS Benchmarks - AWS - Foundations - v1.0.4 - 5.2 Networking - Ensure no security groups allow ingress from 0.0.0.0/0 to remote server administration ports.

## node-imds
Instance Metadata Service Options.

## node-volumes
Encrypted Volumes.

* CIS Benchmarks - AWS - Foundations - v1.0.4 - 2.2.1 Storage - EC2 - Ensure EBS volume encryption is enabled.

## node-sgs
No unrestricted access.

* CIS Benchmarks - AWS - Foundations - v1.0.4 - 5.2 Networking - Ensure no security groups allow ingress from 0.0.0.0/0 to remote server administration ports.

## node-private
No Public IP or DNS Name Attached. Also checking associated route tables for IGW routes was considered but deemed not necessary.

## node-role
Ensure that nodes only have minimal permissions.


# EKS CIS Benchmark Analysis
See [cis-eks.md](cis-eks.md) for an understanding of the exact coverage Sek has.


# Areas Not In Scope
You need to draw the line somewhere as complex services depend on and integrate with other components.

All areas identified should still be cotinuously monitored using various tools or custom checks.

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
