from dnacentersdk import api
import urllib3
urllib3.disable_warnings()


# Run the venv in the Desktop/devnet directory devnetvenv, it has all the install requirements
# for the dnacentersdk
# 'source devnetvenv/bin/activate'

#this creates connection object to DNAC
cssdnac = api.DNACenterAPI(username="admin", password="C1sco12345", base_url="https://198.18.129.100:443", version='1.3.0',verify=False)

# Pull Floor IDs
sites = cssdnac.sites.get_site()

for eachsite in sites["response"]:
    if eachsite['siteNameHierarchy'] == 'Global/Area1/Bldg1/Floor1':
        print('Floor1 site id is ', eachsite['id'])
        # create variable to store siteid
        Floor1siteid = eachsite['id']

    elif eachsite['siteNameHierarchy'] == 'Global/Area1/Bldg1/DC':
        print('DC site id is ', eachsite['id'])
        # create variable to store siteid
        DCsiteid = eachsite['id']


# Assign devices to Floors

# Create Wireless Profiles

#
