from database import data
import app

rows = data.packets.getAllSourceIpAddress()

ip = rows[0]
print(ip)

print(data.geoips.isIpAlreadyRegistered(ip))

if __name__ == '__main__':
  app.run()