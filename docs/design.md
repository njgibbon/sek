# Design


# Checks
MVP Check Set.

## EKS
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
* Nodes - Node Role minimal permissions = IRSA.
* Nodes - Node Role read only access to ECR.

## Areas Not In Scope
* KMS Keys used for any EKS-related encryption are rotated.
* General IAM best practises.
* In-Cluster Kubernetes Security Best Practises.
* Network Audit - VPC Flow Logs.
* Managed Service Actions Audit - CloudTrail.
* CloudWatch CMKs.
* Nodes - VPC Endpoint for ECR.


# Configuration
* CLI Inputs.
* CLI Outputs.
* Config file(s).
* Environment vars.
* Precedence.
* Skip checks.


# Modes
* Atomic / Default.  
* Audit.


# Structure
* Pakage needs to work programatically outside of CLI.
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


# Scratch

main > CheckInit > CheckSet > Check

Kube-bench and sek, checkov with fails situational, how much of cis eks benchmark is left un-automated? And then how much could be?
```
print("Sek - Runtime Cloud Security and Misconfiguration Scanning")
print("-----")
print("Scan")
print("-----")
print("Cloud: " + CLOUD + " - Resource: " + RESOURCE + " - Name: " + NAME)
print("-----")
print("Results")
print("-----")
print("service-logging: PASS")
print("service-secrets: PASS")
print("service-endpoint: PASS")
print("service-endpoint-firewall: PASS")
print("service-security-groups: PASS")
print("nodes-imds: PASS")
print("nodes-volumes: PASS")
print("nodes-security-groups: PASS")
print("nodes-subnets: PASS")
print("nodes-ips: PASS")
print("-----")
print("Stats")
print("-----")
print ("Time: 0.5s")
print("Checks: 10")
print("Passed: 10 - (100.00%)")
print("Failed: 0 - (0.00%)")
print("Skipped: 0 - (0.00%)")
print("Errors: 0 - (0.00%)")
```
