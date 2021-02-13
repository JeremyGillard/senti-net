import requests
import psycopg2

connection = psycopg2.connect(database="sentinet", user="sentinet", password="sentinet", host="127.0.0.1", port="5432")

cursor = connection.cursor()
ips = cursor.execute("SELECT DISTINCT(src) FROM packets WHERE src  NOT LIKE '192.168.1.%'")
rows = cursor.fetchall()
rows = [row[0] for row in rows]

fieldOptions = 'continent,country,regionName,city,district,zip,lat,lon,timezone,isp,org,as,asname,mobile,proxy,hosting,query'.split(',')

url = 'http://ip-api.com/batch?fields=continent,country,regionName,city,district,zip,lat,lon,timezone,isp,org,as,asname,mobile,proxy,hosting,query'
data = rows
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

response = requests.post(url, json=data, headers=headers)

def format_value(entry):
  r = entry
  s = ''
  for value in r:
    if type(r[value]) == str:
      s += f"'{r[value]}', "
    else:
      s += f"{r[value]}, "
  return s[:-2]

columns = 'continent,country,region,city,district,zip,lat,lon,timezone,isp,org,asnumber,asname,mobile,proxy,hosting,query'
for entry in response.json():
  query_selection = f"SELECT * FROM geoips WHERE query LIKE '{entry['query']}'"
  cursor.execute(query_selection)
  if len(cursor.fetchall()) == 0:
    query_insertion = f'INSERT INTO geoips ({columns.lower()}) VALUES ({format_value(entry)})'
    cursor.execute(query_insertion)
connection.commit()

connection.close()

# TEST PURPOSE
# print(rows[0])
# print(response.json()[0].keys())
# print(len(response.json()[0]))
# print(len(fieldOptions))

# for key in fieldOptions:
#   if key not in response.json()[0].keys():
#     print(key)