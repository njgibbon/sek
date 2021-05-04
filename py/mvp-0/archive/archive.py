# Check that all found Subnet IDs are explicitly associated
# If a Subnet is not explicitly associated then it will be implicitly associated to the main RT
# And the Main RT will need to be found and analysed
found_associations = 0
for rt in route_tables["RouteTables"]:
    for a in rt["Associations"]:
        if a["SubnetId"] in subnet_ids:
            found_associations = found_associations+1
if found_associations == len(subnet_ids):
    assert True
else:
    # Find Main Route Table for VPC and Examine
    # ...