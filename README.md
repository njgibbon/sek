![sek](images/sek.png)

Runtime Cloud Security Scanning.

# Status
Concept / Dev / Test / Pre-pre-release. Just trying some things and working out how stuff might fit together.


# Overview
Sek scans live configurations of Cloud Resources.

The intitial focus is only on the Cloud Resource components of AWS EKS, that is the set of security checks that can reliably be automated using the Cloud provider APIs.

The MVP check set is informed by industry standards primarily the Center for Internet Security Benchmarks. See the check documentation section for a comprehensive view. 


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
