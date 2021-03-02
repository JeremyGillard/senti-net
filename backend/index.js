const redis = require('redis');

const db = require('./db');

const subscriber = redis.createClient();

subscriber.on('message', function (channel, message) {
  if (channel === 'packets') {
    const packet = JSON.parse(message);
    insertPacket(packet);
    // console.log(packet);
  }
});

subscriber.subscribe('packets');

async function getData() {
  const result = await db.getSrcIps();
  console.log(result);
}

function exec() {
  getData();
}

exec();
