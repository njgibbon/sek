# Design

## EKS
* Logging - Audit logs.
* Secrets - Envelope Encryption.
* Private Endpoint enabled. Public Endpoint disabled.
* Public Endpoint Firewall if exists.
* Cluster SG - no unrestricted access.
* Additional SGs - no unrestricted access.
* HTTPS - Built In.

## EC2
* Instance Metadata.
* Encrypted Volumes.
* Worker Security Groups.
* Private Subnets.
