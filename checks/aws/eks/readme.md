# EKS Checks

* Service - Logging - Audit logs.
* Service - Secrets - Envelope Encryption.
* Service - Private Endpoint enabled. Public Endpoint disabled.
* Service - Public Endpoint Firewall if exists.
* Service - Cluster SGs - No unrestricted access.
* Nodes - Instance Metadata Service Options.
* Nodes - Encrypted Volumes.
* Nodes - Security Groups.
* Nodes - Private Subnets.
* Nodes - No Public IP or DNS Name Attached.
* Nodes - Node Role minimal permissions.


# Areas Not In Scope
* KMS Keys used for any EKS-related encryption are rotated.
* General IAM best practises.
* In-Cluster Kubernetes Security Best Practises.
* Network Audit - VPC Flow Logs.
* Managed Service Actions Audit - CloudTrail.
* CloudWatch CMKs.
* VPC Endpoint Architecure.
* CIS Hardening of Nodes.


# Resources
* CIS Benchmarks - Kubernetes - EKS - v1.0.1 - https://learn.cisecurity.org/benchmarks
    * https://aws.amazon.com/blogs/containers/introducing-cis-amazon-eks-benchmark/
* AWS EKS Best Practises - Security - https://aws.github.io/aws-eks-best-practices/security/docs/index.html
* AWS EKS Security Documentation - https://docs.aws.amazon.com/eks/latest/userguide/security.html


# Other Resources
* Kube-Bench - https://github.com/aquasecurity/kube-bench
* CIS Benchmarks - AWS - Foundations - v1.0.4 - https://learn.cisecurity.org/benchmarks
