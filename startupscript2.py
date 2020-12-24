from dnacentersdk import api
import urllib3
urllib3.disable_warnings()
from pprint import pprint


# Run the venv in the Desktop/devnet directory devnetvenv, it has all the install requirements
# for the dnacentersdk
# 'source devnetvenv/bin/activate'

#this creates connection object to DNAC
cssdnac = api.DNACenterAPI(username="admin", password="C1sco12345", base_url="https://198.18.129.100:443", version='1.3.0',verify=False)

# Call list of discoveries
discoveries=cssdnac.network_discovery.get_discoveries_by_range(start_index=1,records_to_return=20)

# Get switches and 9800wlc discovery IDs
for discovery in discoveries['response']:
  if discovery['name'] == 'Switches':
    switchdiscoveryid = discovery['id']

  elif discovery['name'] == '9800wlc':
    iosxewlcdiscoveryid = discovery['id']

# Get discovered devices by id
switchdiscoverystate = cssdnac.network_discovery.get_discovered_devices_by_range(id=switchdiscoveryid,start_index=1,records_to_return=20)
iosxewlcdiscoverystate = cssdnac.network_discovery.get_discovered_devices_by_range(id=iosxewlcdiscoveryid,start_index=1,records_to_return=20)

print('These are the discovery restults for switches')
pprint(switchdiscoverystate['response'])

print('These are the discovery restults for 9800 controllers')
pprint(iosxewlcdiscoverystate['response'])


# Get Managed Devices in inventory
devicelist = cssdnac.devices.get_device_list()
for device in devicelist['response']:
    print("hostname:  {}, collectionStatus: {}, reachabilityStatus: {}')".format(device['hostname'],device['collectionStatus'],device['reachabilityStatus']))


print('End of script')
