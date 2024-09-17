# 0a_deploy_NADs.py
#
# This file will create Network Access Devices (NADs) and assign them to the correct Network Device Group (NDG).  .
# You should not need to modify this file as it will dynamically read all of the NADs
# from NADs.yaml.
#
# The group name to group id matching and variable assignment is kind of irritating, but..... 
#
# Actually it's more that ISE requires a group id instead of a group name when creating a user.

import yaml  # import pyyaml package

# open the yaml file and load it into data
with open('credentials.yaml') as f:
    data = yaml.safe_load(f)

# open the groupsandusers.yaml file and load it into groups
with open('NADs.yaml') as g:
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
for nad_group in groups['NADS']:
        api.network_device.create_network_device(authentication_settings=nad_group['auth_settings'],
                                    coa_port=None, 
                                    description=None, 
                                    dtls_dns_name=None, 
                                    model_name=None, 
                                    name=nad_group['name'], 
                                    network_device_group_list=None, 
                                    network_device_iplist=nad_group['ip_addr'], 
                                    profile_name=None, 
                                    snmpsettings=None, 
                                    software_version=None, 
                                    tacacs_settings=None, 
                                    trustsecsettings=nad_group['trustsec'], 
                                    headers=None, 
                                    payload=None, 
                                    active_validation=True)
                # api.internal_user.create_internal_user(name=groupname['name'],
                #                                 first_name=groupname['firstname'],
                #                                 last_name=groupname['lastname'],
                #                                 description=groupname['description'],
                #                                 password=groups['default_password'],
                #                                 change_password=False,
                #                                 identity_groups=groupid,
                #                                 password_idstore="Internal Users")
        print("Creating NAD:", nad_group['name'])