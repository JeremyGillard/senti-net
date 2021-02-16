import app.sniffer as sniffer
import app.geoips as geoips

def run():
  print('Starting the application...')
  #sniffer.run()
  data = geoips.getGeoInformations()
  print(data[0])
