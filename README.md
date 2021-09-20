![sek](images/sek.png)

Live Cloud Resource Security Configuration Scanning.

# Status
Concept / Dev / Test / Pre-pre-release. Trying things and working out how stuff might fit together.


# Overview
Sek scans live Cloud Resources and looks for Security-related misconfiguration.

Sek is intended for immediate fast security feedback when working with a Cloud Service. Simplifying complex Spot Checks and providing Continuous Compliance / Testing via Automated Pipelines.

Comprehensive Audit Capabilities and Integrations will come next. See [roadmap.md](roadmap.md).

Intitially the focus is only on the Cloud Resource components of AWS EKS.

Cloud Resource Check Sets are informed by community best practises and industry standards like the Center for Internet Security Benchmarks. See the Check documentation section for a comprehensive view.


# Checks
Organisation, structure, content, reasoning and support information for all Checks in Sek.

[checks/readme.md](checks/readme.md)

**Example: AWS - EKS**

[checks/aws/eks/readme.md](checks/aws/eks/readme.md)


# Use
## Install
```
pip3 install sek --upgrade
```

## Configure
CLI flags are currently the only way to control the tool.
### Authentication
#### AWS
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

### Skipping Checks
TODO

## Run
```
sek --cloud=aws --resource=eks --name=name
```


# Permissions
Sek will not utilise any write operations for any check with any cloud provider. Read only access permissions will be sufficient.


# Roadmap
[roadmap.md](roadmap.md)


# Contributing
[contributing.md](contributing.md)


# Related Tools
* Prowler - https://github.com/toniblyx/prowler
* Kube-Bench - https://github.com/aquasecurity/kube-bench
* Checkov - https://github.com/bridgecrewio/checkov
* AWS Security Hub - https://aws.amazon.com/security-hub
* AWS Config - https://aws.amazon.com/config
