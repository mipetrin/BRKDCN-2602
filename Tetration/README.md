Created by Michael Petrinovic 2018

Sample Tetration Scripts for Cisco Live Melbourne 2018: BRKDCN-2602

Be sure to download the API Key from your tetration platform. When generating the key, it allows you to specify the access rights for that key. Furthermore, once generated, it allows you to download a JSON file, that contains the 'api_key' and 'api_secret'

Download them, be sure to then specify this file with the -c option.

Sample usage:

Get Users
# python tetration_get_users.py -c kangaroo_sa_credentials.json -p https://kangaroo.cisco.com

Get Sensors
# python tetration_sensors_sw_hw.py -c kangaroo_sa_credentials.json -p https://kangaroo.cisco.com

Get Flows + TopN /// DNS = 53
# python tetration_flow_topN_search.py -c kangaroo_sa_credentials.json -p https://kangaroo.cisco.com --port 53 --limit 500 --hours 24

Get Flows + TopN /// DHCP = 67
# python tetration_flow_topN_search.py -c kangaroo_sa_credentials.json -p https://kangaroo.cisco.com --port 67 --limit 500 --hours 24

Get Flows + TopN /// NTP = 123
# python tetration_flow_topN_search.py -c kangaroo_sa_credentials.json -p https://kangaroo.cisco.com --port 123 --limit 500 --hours 24
