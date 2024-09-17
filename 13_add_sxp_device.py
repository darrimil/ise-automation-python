# 13_add_sxp_device.py
#
# This file will create a SXP device to make sure it's working with IP/SGT
# You should not need to modify this file as it will dynamically read all of the SXP Devices
# from SXP-Device.yaml.
#
# The group name to group id matching and variable assignment is kind of irritating, but..... 
#
# Actually it's more that ISE requires a group id instead of a group name when creating a user.

import yaml  # import pyyaml package

# open the yaml file and load it into data
with open('credentials.yaml') as f:
    data = yaml.safe_load(f)

# open the groupsandusers.yaml file and load it into groups
with open('SXP-Device.yaml') as g:
    groups = yaml.safe_load(g)

# Pull in the Cisco ISE SDK
from ciscoisesdk import IdentityServicesEngineAPI

# define our API 
api = IdentityServicesEngineAPI(username=data['ise_username'], 
                                password=data['ise_password'],
                                uses_api_gateway=True,
                                base_url='https://' + data['ise_hostname'],
                                version=data['ise_version'],
                                verify=data['ise_verify'])

# We're going to iterate through the list of NADs and create them using the information in NADs.yaml,
# but first we need to get the group id for each group
for sxp_conn in groups['SXP-Conns']:
        api.sxp_connections.create_sxp_connections(sxp_peer=sxp_conn['sxpPeer'], 
                                                   enabled=sxp_conn['enabled'], 
                                                   ip_address=sxp_conn['ipAddress'], 
                                                   sxp_mode=sxp_conn['sxpMode'], 
                                                   sxp_node=sxp_conn['sxpNode'],  
                                                   sxp_version=sxp_conn['sxpVersion'], 
                                                   sxp_vpn=sxp_conn['sxpVpn'],
                                                   description=sxp_conn['description']                                                    
                                                )
        print("Creating SXP Connection:", sxp_conn['sxpPeer'])