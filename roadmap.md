# Roadmap


# Status
The `v0.1.x` core focus is to implement and distribute a MVP CLI tool which will perform a set of runtime security checks against the managed service element of AWS EKS.

The checks implemented will be largely sourced from industry standard recommendations and the source, support and reasoning for all checks will be very clear.

The tool will have a good scalable internal structure to enable quality testing and future evolution.


# Now

See Issue Tracker.

https://github.com/njgibbon/sek/issues


# Future

## Features

### Configuration
* File based configuration for Sek as well as Environment Variables.

### Support more resources, more clouds
* Implementing an MVP with only AWS - EKS in mind. I would like to add more AWS services and even more clouds. So, after getting the core logic down the internal structure will focus on enabling reuse of the same patterns, interfaces and testing to make this sort of extentsion natural and relatively easy.
* It may make the most sense to pivot to support Azure - AKS and GCP - GKE aswell as AWS - EKS to make Sek a more general Managed Kubernetes Security Scanner!

### Audit mode
* Initial focus on a scan against one single service given a name. In the future this can be extended to audit for all resources of the resource type in an account or region.
