from dnacentersdk import api
import urllib3
urllib3.disable_warnings()


# Run the venv in the Desktop/devnet directory devnetvenv, it has all the install requirements
# for the dnacentersdk
# 'source devnetvenv/bin/activate'

#this creates connection object to DNAC
cssdnac = api.DNACenterAPI(username="admin", password="C1sco12345", base_url="https://198.18.129.100:443", version='1.3.0',verify=False)

#cli payload
cli = [{'description': 'this is a new cli from the python sdk',
    'enablePassword': 'C1sco12345', 'password': 'C1sco12345',
    'username': 'dnacadmin'}]
print('Creating cli credential payload')

#create cli
cssdnac.network_discovery.create_cli_credentials(payload=cli)
print('Creating credentials')

#snmp read payload
snmpread = [{'description': 'read', 'readCommunity': 'read'}]
print('Creating snmp read credential payload')

#create snmpread
cssdnac.network_discovery.create_snmp_read_community(payload=snmpread)
print('Creating snmp read credentials')

#create snmpwrite
snmpwrite = [{'description': 'write', 'writeCommunity': 'write'}]
print('Creating snmp write credential payload')

cssdnac.network_discovery.create_snmp_write_community(payload=snmpwrite)
print('Creating snmp write credentials')

#define site payloads
Area1 = { "type": "area", "site": { "area":
            { "name": "Area1", "parentName": "Global"
        }}}
print('Creating Area1 payload')

Bldg1 = { "type": "building", "site": { "building": {
              "name": "Bldg1",
              "address": "New York, United States",
              "parentName": "Global/Area1",
              "latitude": 43.000000,
              "longitude": -75.000000
        }}}
print('Creating Bldg1 payload')

Floor1 = { "type": "floor", "site": { "floor": {
            "name": "floor1",
            "parentName": "Global/Area1/Bldg1",
            "rfModel": "Cubes And Walled Offices",
            "width": 100,
            "length": 200,
            "height": 15
        }}}

print('Creating Floor1 payload')

DC = { "type": "floor", "site": { "floor": {
            "name": "DC",
            "parentName": "Global/Area1/Bldg1",
            "rfModel": "Cubes And Walled Offices",
            "width": 100,
            "length": 200,
            "height": 15
        }}}

#create Area1
cssdnac.sites.create_site(payload=Area1)
print('Creating Area1')
#create Bldg1
cssdnac.sites.create_site(payload=Bldg1)
print('Creating Bldg1')
#create floor1
cssdnac.sites.create_site(payload=Floor1)
print('Creating Floor1')
#create DC
cssdnac.sites.create_site(payload=DC)
print('Creating DC')

#start switch discovery
cssdnac.network_discovery.start_discovery(
                        discoveryType="Multi range",
                        enablePasswordList=["C1sco12345"],
                        ipAddressList="172.16.102.2-172.16.102.10",
                        name="Switches",
                        passwordList=["C1sco12345"],
                        preferredMgmtIPMethod=None,
                        protocolOrder="ssh",
                        retry=3,
                        snmpROCommunity="read",
                        snmpROCommunityDesc="read",
                        snmpRWCommunity="write",
                        snmpRWCommunityDesc="write",
                        snmpVersion="SNMPv2c",
                        timeout=5,
                        userNameList=["dnacadmin"])

print('Starting switch discovery')

#start 9800wlc discovery
cssdnac.network_discovery.start_discovery(
                        discoveryType="Multi range",
                        enablePasswordList=["C1sco12345"],
                        ipAddressList="198.18.134.100-198.18.134.100",
                        name="9800wlc",
                        passwordList=["C1sco12345"],
                        preferredMgmtIPMethod=None,
                        protocolOrder="ssh",
                        retry=3,
                        snmpROCommunity="read",
                        snmpROCommunityDesc="read",
                        snmpRWCommunity="write",
                        snmpRWCommunityDesc="write",
                        snmpVersion="SNMPv2c",
                        netconfPort="830",
                        timeout=5,
                        userNameList=["dnacadmin"])

print('Starting 9800wlc discovery')

#start 3504wlc discovery
cssdnac.network_discovery.start_discovery(
                        discoveryType="Multi range",
                        enablePasswordList=["C1sco12345"],
                        ipAddressList="172.16.18.5-172.16.18.5",
                        name="3504wlc",
                        passwordList=["C1sco12345"],
                        preferredMgmtIPMethod=None,
                        protocolOrder="ssh",
                        retry=3,
                        snmpROCommunity="read",
                        snmpROCommunityDesc="read",
                        snmpRWCommunity="write",
                        snmpRWCommunityDesc="write",
                        snmpVersion="SNMPv2c",
                        timeout=5,
                        userNameList=["dnacadmin"])

print('Starting 3504wlc discovery')

print('End of script!')
