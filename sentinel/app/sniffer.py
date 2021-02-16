from scapy.all import sniff, IP
from datetime import datetime
from copy import deepcopy

class Packet:
  def __init__(self, src, sport, dst, dport, proto, iteration = 0):
    self.id = f'{src}:{sport}-{dst}:{dport}'
    self.src = src
    self.sport = sport
    self.dst = dst
    self.dport = dport
    self.proto = proto
    self.iteration = iteration

  def __str__(self):
    return f'{self.src:15}:{self.sport:<5} - {self.dst:15}:{self.dport:<5} - {self.iteration:9}'

  def header(self):
    return f'{"src":15}:{"sport":<5} - {"dst":15}:{"dport":<5} - iteration - [Header]'

class Sniffer:
  def __init__(self):
    self.packets_buffer = {}
    self.display_count = 0
    self.reference_time = datetime.now()

  def listen(self):
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
      print(f'{"Datetime":28} {packet.header()}')
    packet = self.packets_buffer[packet.id]
    print(f'[{time}] {packet}')
    self.display_count += 1

  def bufferize(self, packet):
    if packet.id in self.packets_buffer:
      self.packets_buffer[packet.id].iteration += 1
    else:
      packet.iteration = 1
      self.packets_buffer[packet.id] = packet

  def store(self):
    pass
