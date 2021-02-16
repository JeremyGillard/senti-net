import psycopg2

connection = psycopg2.connect(database="sentinet", user="sentinet", password="sentinet", host="127.0.0.1", port="5432")
cursor = connection.cursor()

class Packets:
  def getAllSourceIpAddress(self):
    ips = cursor.execute("SELECT DISTINCT(src) FROM packets WHERE src  NOT LIKE '192.168.1.%'")
    rows = cursor.fetchall()
    return [row[0] for row in rows]

packets = Packets()

class GeoIps:
  def isIpAlreadyRegistered(self, ip):
    cursor.execute("SELECT * FROM geoips WHERE query LIKE %s", (ip,))
    rows = cursor.fetchall()
    return len(rows) != 0

geoips = GeoIps()