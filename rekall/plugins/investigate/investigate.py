# Query OpenDNS's Investigate API for domain name classifications

__author__ = "OpenDNS"

import requests
import json
from rekall.plugins.investigate.investigate_credentials import api_key

uri = "https://investigate.api.opendns.com"
headers = {'Authorization': 'Bearer ' + api_key}
statuses = {1: 'Whitelisted', 0: 'Unknown', -1: 'Blacklisted'}

def check_name(name):
    url = uri + '/domains/categorization/'

    if name.endswith('\x00'):
        n = name.strip('\x00')
    else:
        n = name
    resp = requests.post(url, headers=headers, data=json.dumps([n]))
	
    if resp.status_code == 200:
        results = resp.json()
        return statuses[results[n]['status']]
    else:
        return "InvestigateErr"
