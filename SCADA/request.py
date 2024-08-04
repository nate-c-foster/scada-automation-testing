import requests
import urllib.parse



def all_locations():

    x = requests.get('http://localhost:8088/system/webdev/SCADA_API/api/location-all')
    if x.status_code == 200:
        return x.json()
    else:
        return []

def location_details(location_id):
    x = requests.get('http://localhost:8088/system/webdev/SCADA_API/api/location-details', params={'locationID':location_id})
    
    if x.status_code == 200:
        return x.json()
    else:
        return {}

def tag_read(tagPath):

    encodedPath = urllib.parse.quote(tagPath)
    x = requests.get('http://localhost:8088/system/webdev/SCADA_API/api/tag-read', params={'tagPath':encodedPath})
    
    if x.status_code == 200:
        return x.json()
    else:
        return {}
    

#print(location_details(64))
#print(all_locations())
#print(tag_read('[SCADA]SIM City/Distribution/Booster PS/Pressure/Control/DeviceStatus/Output')['value'])