![sek](images/sek.png)

Runtime Cloud Security Scanning.

# Status
Concept / Dev / Test / Pre-pre-release. Just trying some things and working out how stuff might fit together.


# Overview
TODO


# Checks
Organisation, structure, content, reasoning and support information for all Checks in Sek.

[checks/readme.md](checks/readme.md)

**Example: AWS - EKS**

[checks/aws/eks/readme.md](checks/aws/eks/readme.md)


# Use

## Install
```
pip3 install sek
```

## Configure
CLI flags are currently the only way to control the tool.
### Authentication
#### AWS
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

## Run
```
sek --cloud=aws --resource=eks --name=test
```


# Roadmap
[docs/roadmap.md](docs/roadmap.md)

# Contributing
[contributing.md](contributing.md)


# Related Tools
* Prowler - https://github.com/toniblyx/prowler
* Kube-Bench - https://github.com/aquasecurity/kube-bench
* Checkov - https://github.com/bridgecrewio/checkov
