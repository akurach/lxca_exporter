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
    print("chassis: " + item['deviceName']) # get chasis
    tr = objectpath.Tree(item['children'])
    t2 = tuple(tr.execute('$..children'))
    for device in t2:
        if 'deviceType' in device:
            print("sn: " + device['serialNumber'])
            print("End Date: " + device['endDate'])
            print("Status: " + device['status'])
            