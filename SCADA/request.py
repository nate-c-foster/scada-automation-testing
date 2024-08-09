import requests
import urllib.parse

from config import GATEWAY_IP
from config import API_PROJECT_NAME
from config import MODEL_TAG_PATH 


def all_locations():

    x = requests.get('http://{gateway_ip}:8088/system/webdev/{api_project_name}/api/location-all'.format(gateway_ip=GATEWAY_IP, api_project_name=API_PROJECT_NAME), 
                     params={'modelTagPath':MODEL_TAG_PATH})
    if x.status_code == 200:
        return x.json()
    else:
        return []

def location_details(location_id):
    x = requests.get('http://{gateway_ip}:8088/system/webdev/{api_project_name}/api/location-details'.format(gateway_ip=GATEWAY_IP, api_project_name=API_PROJECT_NAME), 
                     params={'locationID':location_id,'modelTagPath':MODEL_TAG_PATH})
    
    if x.status_code == 200:
        return x.json()
    else:
        return {}

def tag_to_css_id(tagPath):

    encodedPath = urllib.parse.quote(tagPath)
    x = requests.get('http://{gateway_ip}:8088/system/webdev/{api_project_name}/api/tag-to-css-id'.format(gateway_ip=GATEWAY_IP, api_project_name=API_PROJECT_NAME), 
                     params={'tagPath':encodedPath})
    
    if x.status_code == 200:
        return x.json()['cssId']
    else:
        return {}
    

# print(location_details(64))
# print(all_locations())
# print(tag_read('[SCADA]SIM City/Distribution/Booster PS/Pressure/Control/DeviceStatus/Output')['value'])
# print(tag_to_css_id('[SCADA]SIM City/Distribution/Booster PS/Pressure/Control/DeviceStatus/Output')['cssId'])