from scapy.all import sniff, IP
from datetime import datetime

class Packet:
  def __init__(self, src, sport, dst, dport, proto):
    self.id = f'{src}:{sport} - {dst}:{dport}'
    self.src = src
    self.sport = sport
    self.dst = dst
    self.dport = dport
    self.proto = proto

  def __str__(self):
    return f'{self.src:15}:{self.sport:<5} - {self.dst:15}:{self.dport:<5}'

  def header(self):
    return f'{"src":15}:{"sport":<5} - {"dst":15}:{"dport":<5}'

class Sniffer:
  def __init__(self):
    self.display_count = 0
    self.packets_buffer = {}
    self.reference_time = datetime.now()

  def listen(self, display = False):
    sniff(prn=self.process)

  def process(self, scapy_pkt):
    if scapy_pkt.haslayer(IP) and hasattr(scapy_pkt.payload, "sport"):
      packet = Packet(scapy_pkt[IP].src, scapy_pkt.sport, scapy_pkt[IP].dst, scapy_pkt.dport, scapy_pkt.proto)
      self.bufferize(packet)
      self.display(packet)
      self.store()

  def display(self, packet):
    time = datetime.now()
    if (self.display_count > 20):
      self.display_count = 0
    if (self.display_count == 0):
      print(f'{"Datetime":28} {packet.header()}    [header]')
    print(f'[{time}] {packet}')
    self.display_count += 1

  def bufferize(self, packet):
    pass

  def store(self):
    pass
