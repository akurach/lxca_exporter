'''
@since: 5 July 2018
@author: Kurach Aleksandr <sundelor@gmail.com>
@license: GPL
@summary: Warranty check for PyLXCA
'''
import sys
import requests
from requests.auth import HTTPBasicAuth
import simplejson as json
import objectpath
from variable import *

r = requests.get(ip+url_warranty, auth=HTTPBasicAuth(user, passwd), verify=False)
d = json.loads(r.text)

for item in d:
    print("Chassis Name: " + item['deviceName']) # get chasiss
    print("Status: " + item['status'])
    print("End Date: " + item['endDate'])
    print()
    tr = objectpath.Tree(item['children'])
    t2 = tuple(tr.execute('$..children'))
    for device in t2:
        if 'deviceType' in device:
            print("Node Name: " + device['deviceName'])
            print("sn: " + device['serialNumber'])
            print("Status: " + device['status'])
            print("End Date: " + device['endDate'])
            print()

