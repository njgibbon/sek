# Roadmap


# Status
The v0.1.* core focus is to implement and distribute a MVP CLI tool which will perform a set of runtime security checks against the managed service element of AWS EKS.

The checks implemented will be largely sourced from industry standard recommendations and the source, support and reasoning for all checks will be very clear.

The tool will have a *decent* scalable internal structure.

After this has been achieved then below is a list of things that I am thinking about.


# Features

## Configuration
File based configuration for Sek aswell as environment variables. Import to also enable check skip functionality.

## Support more resources, more clouds
Implementing an MVP with only AWS - EKS in mind. I would like to add more AWS services and even more clouds. So, after getting the core logic down the internal structure will focus on enabling reuse of the same patterns, interfaces and testing to make this sort of extentsion natural and relatively easy.

## Audit mode
Initial focus on a scan against one single service given a name. In the future this can be extended to audit for all services in an account or region.


# Technical

## Version pinning
Version pinning of dependencies.

## Release
More complete metadata for v0.1.x+ PyPy releases and usage of a consistent process mapping to GitHub Releases.

## Unit testing
The nature of the problem requires authenticated access to remote cloud APIs for core function. How can I best implement

## Functional testing
What can be done around automation and functional testing given cost constraints? Start with some automation that is run manually and go from there I expect.

## Automation
More automation of testing and other things.

## Documentation
Complete a good deal of documentation to provide support to users and contributors. Including support documentation to show different ways of integrating the tool into workflows or with other tools.

## Debt
Any technical debt in the issue tracker or otherwise.

## Defects
Any defects in the issue tracker or otherwise.

## Ideas
Any ideas that come up. For example, maybe multi-threading all checks would be a good improvement? Maybe this would add complexity but little value.
