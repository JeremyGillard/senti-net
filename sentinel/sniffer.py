from scapy.all import *
import psycopg2
import requests
import datetime

connection = psycopg2.connect(database="sentinet", user="sentinet", password="sentinet", host="127.0.0.1", port="5432")

def prettyPrint(pkt):
  time=datetime.datetime.now()

  if pkt.haslayer(IP):
    #response = requests.get(f'http://ip-api.com/json/{str(pkt[IP].src)}')
    print(f'{str(time)} - {str(pkt[IP].src)}:{str(pkt.sport)}')
    #print(response.json())

if __name__ == '__main__':
  sniff(prn=prettyPrint)
