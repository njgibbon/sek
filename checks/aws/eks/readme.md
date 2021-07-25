# EKS Checks

## service-logging
Audit logs should be enabled. Logs provide visibility into operation of the service. From a Security perspective they can be analysed automatically or otherwise to understand anomolous or unexpected use of the service.

* https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html
* CIS Benchmarks - Kubernetes - EKS - v1.0.1 - 2.1.1 - Control Plane Configuration - Logging - Enable audit Logs

## service-secrets
Envelope encryption for Kubernetes Secrets with KMS.

* https://aws.amazon.com/blogs/containers/using-eks-encryption-provider-support-for-defense-in-depth/
* CIS Benchmarks - Kubernetes - EKS - v1.0.1 - 5.3.1 Ensure Kubernetes Secrets are encrypted using Customer Master Keys (CMKs) managed in AWS KMS.

## service-endpoint
Private Endpoint enabled. Public Endpoint disabled. It is more secure to design a network architecture such that you do not need to access the Kubernetes API via the public internet.

* https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html
* CIS Benchmarks - Kubernetes - EKS - v1.0.1 - 5.4.2 Ensure clusters are created with Private Endpoint Enabled and Public Access Disabled.

## service-endpoint-firewall
If a public EKS endpoint exists then ensure that there is no unrestricted access.

* https://aws.amazon.com/about-aws/whats-new/2019/12/amazon-eks-enables-network-access-restrictions-to-kubernetes-cluster-public-endpoints/

## service-sgs
No unrestricted inbound access to the control-plane. Security Groups can restrict access based on range, port and protocol. This check ensures that at least some restriction is being used. You should implement further restriction.

* https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html
* CIS Benchmarks - AWS - Foundations - v1.0.4 - 5.2 Networking - Ensure no security groups allow ingress from 0.0.0.0/0 to remote server administration ports.

## node-imds
The Instance Metadata Service is where EC2 Instances obtain Role Security Credentials. If it is not needed then it should be disabled. For EKS, some AWS access will always be needed. IMDSv2 uses session-oriented access and so is more secure. A Hop limit of 1 will restrict access to a signle network hop and so workloads running in the container the cluster network will not be able to talk to the service. In combination with **node-role** this means that in-cluster workloads must use IAM Roles for Service Accounts to access AWS Resources.

* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html
* https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html
* https://docs.aws.amazon.com/eks/latest/userguide/best-practices-security.html#restrict-ec2-credential-access
* CIS Benchmarks - Kubernetes - EKS - v1.0.1 - 5.2.1 Managed services - IAM - Prefer using dedicated EKS Service Accounts

## node-volumes
Volumes attached to instances can include root volumes and other volumes as well as volumes which are controlled by things like Kubernetes Storage Classes for in-cluster Persistant Volumes. All of these should be encrypted at rest.

* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html
* CIS Benchmarks - AWS - Foundations - v1.0.4 - 2.2.1 Storage - EC2 - Ensure EBS volume encryption is enabled.

## node-sgs
No unrestricted inbound access to the nodes. Security Groups can restrict access based on range, port and protocol. This check ensures that at least some restriction is being used. You should implement further restriction.

* https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html
* CIS Benchmarks - AWS - Foundations - v1.0.4 - 5.2 Networking - Ensure no security groups allow ingress from 0.0.0.0/0 to remote server administration ports.

## node-private
Nodes should always reside in a private subnet. Where public access is required then services on nodes can be exposed via LoadBalancers. This check ensures that nodes have no Public IP or Public DNS Name Attached. Also checking associated route tables for IGW routes was considered but deemed not necessary.

* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-private-addresses

## node-role
Ensure that nodes only have minimal permissions to access AWS resources. AWS defines the minimal AWS-managed policies for an EKS cluster to function and so this is used to inform this check. This does verify that the nodes only have read-access to ECR but goes further in ensuring nodes follow the core security principle of least priviledge.

* https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html
* CIS Benchmarks - Kubernetes - EKS - v1.0.1 - 5.1.3 Managed Services - Images - Minimize cluster access to read-only for Amazon ECR


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
* Network architecture and VPC Endpoints. https://docs.aws.amazon.com/eks/latest/userguide/private-clusters.html
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
