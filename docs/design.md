# Design

# Checks
MVP Check Set.

## EKS
* Service - Logging - Audit logs.
* Service - Secrets - Envelope Encryption.
* Service - Private Endpoint enabled. Public Endpoint disabled.
* Service - Public Endpoint Firewall if exists.
* Service - Cluster SG - No unrestricted access.
* Service - Additional SGs - No unrestricted access.
* Service - HTTPS - Built In.
* Nodes - Instance Metadata Service Options.
* Nodes - Encrypted Volumes.
* Nodes - Security Groups.
* Nodes - Private Subnets.
* Nodes - No Public IP or DNS Name Attached.

## Other Areas Not In Scope
* KMS Keys used for any EKS-related encryption are rotated.
* General IAM best practises.
* In-Cluster Kubernetes Security Best Practises.
* Network Audit - VPC Flow Logs.
* Managed Service Actions Audit - CloudTrail.

# Configuration
* CLI Inputs.
* CLI Outputs.
* Config file.
* Environment vars.
* Precedence.
* Skip checks.
* Target tags.

# Modes
* Audit.
* Atomic / Default.

# Language
* Py.

# Structure
* CheckSets.
* Checks.
* Tagging system.
* Testing.
* Areas of self-containment / independence vs. efficiencies of grouping.

# AWS Permissions
* Minimal permissions per check-set and config and examples.

# Documentation
* Overview.
* Contributing.

# Automation
* Process.
* Publication.
* Enablement structures.
* Further testing.

