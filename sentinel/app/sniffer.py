from scapy.all import sniff, IP
from datetime import datetime
from database import data

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
    self.schedule_value = 0
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
    if (self.schedule_value > 100):
      self.schedule_value = 0
    if (self.schedule_value % 20 == 0):
      print(f'{"Datetime":28} {packet.header()}')
    packet = self.packets_buffer[packet.id]
    print(f'[{time}] {packet}')
    self.schedule_value += 1

  def bufferize(self, packet):
    if packet.id in self.packets_buffer:
      self.packets_buffer[packet.id].iteration += 1
    else:
      packet.iteration = 1
      self.packets_buffer[packet.id] = packet

  def store(self):
    if self.schedule_value == 100:
      for key in self.packets_buffer:
        current_packet = self.packets_buffer[key]
        recorded_packet = data.packets.getPacket(current_packet.src, str(current_packet.sport), current_packet.dst, str(current_packet.dport))
        if recorded_packet is None:
          data.packets.postPacket(current_packet.src, str(current_packet.sport), current_packet.dst, str(current_packet.dport), current_packet.proto, current_packet.iteration)
        else:
          data.packets.updatePacketIteration(recorded_packet[0], current_packet.iteration + recorded_packet[6])

def run():
  sniffer = Sniffer()
  sniffer.listen()
