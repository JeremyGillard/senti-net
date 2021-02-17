import redis

r = redis.Redis(host='localhost', port='6379', db=0)

p = r.pubsub()

def handler(message):
  print(message)

p.psubscribe(**{'packets':handler})

thread = p.run_in_thread(sleep_time=0.001)