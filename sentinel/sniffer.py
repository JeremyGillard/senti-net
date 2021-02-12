from scapy.all import *
# import requests
from datetime import datetime
from db import connection

in_mem_db = {}
previous_time = datetime.now()
cursor = connection.cursor()

class Data:
  def __init__(self, time, src, sport, dst, dport, proto, iteration):
    self.time = time
    self.src = src
    self.sport = sport
    self.dst = dst
    self.dport = dport
    self.proto = proto
    self.iteration = iteration

  def __str__(self):
    return f'{self.time} - {self.src}:{self.sport} - {self.dst}:{self.dport} - {self.iteration}'

def store_in_memory(time, src, sport, dst, dport, proto):
  id = f'{src}:{sport} - {dst}:{dport}'
  if id in in_mem_db:
      in_mem_db[id].iteration += 1
  else:
    in_mem_db[id] = Data(time, src, sport, dst, dport, proto, 1)
  schedule_storage()

def schedule_storage():
  global previous_time
  if (datetime.now() - previous_time).seconds > 60:
    previous_time = datetime.now()
    print('****************************************** FETCH ******************************************')
    insertData()

def insertData():
  global in_mem_db
  for key in in_mem_db:
    current_element = in_mem_db[key]
    cursor.execute(f"SELECT * FROM packets WHERE src LIKE '{current_element.src}' AND sport LIKE '{current_element.sport}' AND dst LIKE '{current_element.dst}' AND dport LIKE '{current_element.dport}'")
    rows = cursor.fetchall()
    if len(rows) != 0:
      print(*rows[0])
      cursor.execute(f"UPDATE packets SET iteration = {rows[0][6] + current_element.iteration} WHERE id = {rows[0][0]}")
    else:
      cursor.execute(f"INSERT INTO packets (src, sport, dst, dport, proto, iteration) VALUES ('{current_element.src}', '{current_element.sport}', '{current_element.dst}', '{current_element.dport}', {current_element.proto}, {current_element.iteration})")
  connection.commit()
  in_mem_db = {}

def processing(pkt):
  time=datetime.now()

  if pkt.haslayer(IP) and hasattr(pkt.payload, "sport"):
    store_in_memory(time, pkt[IP].src, pkt.sport, pkt[IP].dst, pkt.dport, pkt.proto)
    print(len(in_mem_db))

    #response = requests.get(f'http://ip-api.com/json/{str(pkt[IP].src)}')
    #print(response.json())

if __name__ == '__main__':
  sniff(prn=processing)
