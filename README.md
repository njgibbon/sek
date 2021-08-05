![sek](images/sek.png)

Live Cloud Resource Security Configuration Scanning.

# Status
Concept / Dev / Test / Pre-pre-release. Just trying things and working out how stuff might fit together.


# Overview
Sek scans live Cloud Resources and looks for Security-related misconfiguration.

Intitially, the focus is on the Cloud Resource components of AWS EKS.

Cloud Resource Check Sets are informed by industry standards primarily the Center for Internet Security Benchmarks. See the Check documentation section for a comprehensive view. 


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

## Run
```
sek --cloud=aws --resource=eks --name=name
```


# Permissions
Sek will not utilise any write operations for any check with any cloud provider. Read only access permissions will be sufficient.


# Roadmap
[docs/roadmap.md](docs/roadmap.md)


# Contributing
[contributing.md](contributing.md)


# Related Tools
* Prowler - https://github.com/toniblyx/prowler
* Kube-Bench - https://github.com/aquasecurity/kube-bench
* Checkov - https://github.com/bridgecrewio/checkov
