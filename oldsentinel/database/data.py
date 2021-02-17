import psycopg2
import sys

connection = None

try:
  connection = psycopg2.connect(database="sentinet", user="sentinet", password="sentinet", host="127.0.0.1", port="5432")
except psycopg2.OperationalError as er:
  print('[error] Connection to database failed:\n\n', er)
  sys.exit()

cursor = connection.cursor()

class Packets:
  def getAllSourceIpAddress(self):
    ips = cursor.execute("SELECT DISTINCT(src) FROM packets WHERE src NOT LIKE '192.168.1.%'")
    rows = cursor.fetchall()
    return [row[0] for row in rows]

  def getPacket(self, src, sport, dst, dport):
    cursor.execute("SELECT * FROM packets WHERE src LIKE %s AND sport LIKE %s AND dst LIKE %s AND dport LIKE %s", (src, sport, dst, dport))
    packet = cursor.fetchone()
    return packet

  def postPacket(self, src, sport, dst, dport, proto, iteration):
    cursor.execute("INSERT INTO packets (src, sport, dst, dport, proto, iteration) VALUES (%s, %s, %s, %s, %s, %s)", (src, sport, dst, dport, proto, iteration))
    connection.commit()

  def updatePacketIteration(self, id, iteration):
    cursor.execute("UPDATE packets SET iteration = %s WHERE id = %s", (iteration, id))
    connection.commit()


packets = Packets()

class GeoIps:
  def isIpAlreadyRegistered(self, ip):
    cursor.execute("SELECT * FROM geoips WHERE query LIKE %s", (ip,))
    rows = cursor.fetchall()
    return len(rows) != 0

  def postGeoip(self, continent, country, region, city, lat, lon, isp, org, asname, mobile, hosting, proxy, query):
    cursor.execute("INSERT INTO geoips (continent, country, region, city, lat, lon, isp, org, asname, mobile, hosting, proxy, query) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (continent, country, region, city, lat, lon, isp, org, asname, mobile, hosting, proxy, query))
    connection.commit()

geoips = GeoIps()