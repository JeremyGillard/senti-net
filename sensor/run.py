from scapy.all import sniff, IP
from datetime import datetime
import redis
import json

def translate_proto(proto):
  if proto == 6:
    return 'TCP'
  elif proto == 17:
    return 'UDP'
  else:
    return 'Unknown'

class Packet:
  def __init__(self, src, sport, dst, dport, proto):
    self.time = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    self.src = src
    self.sport = sport
    self.dst = dst
    self.dport = dport
    self.proto = translate_proto(proto)

  def __str__(self):
    return json.dumps(self.__dict__)

  def json(self):
    return json.dumps(self.__dict__).encode('utf8')


class Sniffer:
  def __init__(self, redis):
    self.redis = redis

  def listen(self):
    sniff(prn=self.process)

  def process(self, scapy_pkt):
    if scapy_pkt.haslayer(IP) and hasattr(scapy_pkt.payload, "sport"):
      packet = Packet(scapy_pkt[IP].src, scapy_pkt.sport, scapy_pkt[IP].dst, scapy_pkt.dport, scapy_pkt.proto)
      self.redis.publish('packets', packet.json())


if __name__ == '__main__':
  r = redis.Redis(host='localhost', port='6379', db=0)
  sniffer = Sniffer(r)
  sniffer.listen()