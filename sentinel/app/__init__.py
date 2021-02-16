from app.sniffer import Sniffer

sniffer = Sniffer()

def run():
  print('running the app...')
  sniffer.listen()