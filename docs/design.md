# Design

# Checks
MVP Check Set.

## EKS

### Control Plane
* Logging - Audit logs.
* Secrets - Envelope Encryption.
* Private Endpoint enabled. Public Endpoint disabled.
* Public Endpoint Firewall if exists.
* Cluster SG - no unrestricted access.
* Additional SGs - no unrestricted access.
* HTTPS - Built In.

### Nodes
* Instance Metadata Service Options.
* Encrypted Volumes.
* Node Security Groups.
* Private Subnets.
