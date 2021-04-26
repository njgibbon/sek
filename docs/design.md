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
* Py / Go.

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

