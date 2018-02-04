#!/usr/bin/env python
'''
Very simple script to take an input of MAC Addresses and find out the MAC Vendor
by calling an API to check the specific MAC address

Written by Michael Petrinovic 2018
'''
import requests

MAC_LIST = ["84:B2:61:11:12:13", "d4:6d:50:11:12:13", "f4:4e:05:11:12:13",
            "f4:5c:89:11:12:13", "00:50:56:11:12:13", "00:00:00:11:12:13",
            "00:87:01:11:12:13", "00:14:4F:11:12:13", "00:D9:D1:11:12:13"]

for MAC in MAC_LIST:
    url = "http://api.macvendors.com/" + MAC

    response = requests.request("GET", url)
    print "MAC: " + MAC + " is from Vendor: " + response.text
