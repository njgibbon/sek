# Design


# Features
See [../roadmap.md](../roadmap.md).


# Decisions
See [decisions.md](decisions.md).


# Checks
See [../checks/aws/eks/readme.md](../checks/aws/eks/readme.md).


# Output Design
```
Sek - Runtime Cloud Security Scanning
-----
Cloud: aws - Resource: eks - Name: test
-----
Scan
-----
service-logging: PASS
service-secrets: PASS
-----
Check Document: https://github.com/njgibbon/sek/blob/main/checks/aws/eks
-----
Stats
-----
Time: 0.28124451637268066s
Checks: 2
Pass: 2 - (100.0%)
Fail: 0 - (0.0%)
Error: 0 - (0.0%)
```

# Structure
* Main - Entrypoint - Obtain user input and configuration. Create minimal required objects. Cloud Provider Object.
* ...