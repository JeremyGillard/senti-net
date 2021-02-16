from database import data
import requests

url = 'http://ip-api.com/batch?fields=continent,country,regionName,city,lat,lon,isp,org,as,mobile,proxy,hosting,query'
data = data.packets.getAllSourceIpAddress()
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

def getGeoInformations():
  response = requests.post(url, json=data, headers=headers)
  return response.json()