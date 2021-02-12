from scapy.all import *
# import requests
from datetime import datetime
from db import connection

in_mem_db = {}
previous_time = datetime.now()

class Data:
  def __init__(self, time, src, sport, dst, dport, iteration):
    self.time = time
    self.src = src
    self.sport = sport
    self.dst = dst
    self.dport = dport
    self.iteration = iteration

  def __str__(self):
    return f'{self.time} - {self.src}:{self.sport} - {self.dst}:{self.dport} - {self.iteration}'

def store_in_memory(time, src, sport, dst, dport):
  id = f'{src}:{sport} - {dst}:{dport}'
  if id in in_mem_db:
      in_mem_db[id].iteration += 1
  else:
    in_mem_db[id] = Data(time, src, sport, dst, dport, 1)
  schedule_storage()
  return in_mem_db[id]

def schedule_storage():
  global previous_time
  if (datetime.now() - previous_time).seconds > 60:
    previous_time = datetime.now()
    print('****************************************** FETCH ******************************************')
    print(in_mem_db)


def processing(pkt):
  time=f'{datetime.now()}+00:00'

  if pkt.haslayer(IP) and hasattr(pkt.payload, "sport"):
    current_data = store_in_memory(time, pkt[IP].src, pkt.sport, pkt[IP].dst, pkt.dport)
    print(current_data)

    #response = requests.get(f'http://ip-api.com/json/{str(pkt[IP].src)}')
    #print(response.json())

if __name__ == '__main__':
  sniff(prn=processing)

  # cursor = connection.cursor()
  # cursor.execute('SELECT * FROM packets')
  # rows = cursor.fetchall()

  # for row in rows:
  #   print(*row)

  # connection.close()
