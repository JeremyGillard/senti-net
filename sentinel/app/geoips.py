import threading
import requests
from database import data

url = 'http://ip-api.com/batch?fields=continent,country,regionName,city,lat,lon,isp,org,as,mobile,proxy,hosting,query'
ips = data.packets.getAllSourceIpAddress()
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

def getGeoInformations():
  response = requests.post(url, json=ips, headers=headers)
  return response.json()

def storeGeoIps():
  for entry in getGeoInformations():
    if not data.geoips.isIpAlreadyRegistered(entry['query']):
      data.geoips.postGeoip(entry['continent'], entry['country'], entry['regionName'], entry['city'], entry['lat'], entry['lon'], entry['isp'], entry['org'], entry['as'], entry['mobile'], entry['proxy'], entry['hosting'], entry['query'])
