def unrestricted_security_groups_ingress(sgs):
    """If Protocol, Ports and Range conjunction is *"""
    for sg in sgs["SecurityGroups"]:
        for ip in sg["IpPermissions"]:
            any_protocol = False
            any_port = False
            any_range = False
            # Protocol
            if 'FromPort' not in ip.keys():
                any_protocol = True
            # Port
            if ip["IpProtocol"] == "-1":
                any_port = True
            # Range
            for ipv4_range in ip["IpRanges"]:
                if ipv4_range["CidrIp"] == "0.0.0.0/0":
                    any_range = True
            if any_protocol and any_port and any_range:
                return True
    return False
