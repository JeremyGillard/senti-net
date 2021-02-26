const redis = require('redis');
const axios = require('axios');

const db = require('./db');

const subscriber = redis.createClient();

async function insertPacket(packet) {
  try {
    const query = {
      text:
        'INSERT INTO packets (capture_datetime, src, sport, dst, dport, proto) VALUES ($1, $2, $3, $4, $5, $6)',
      values: Object.values(packet),
    };

    await db.query(query);
  } catch (error) {
    console.error(error);
  }
}

async function getSrcIps() {
  try {
    const query = {
      text: 'SELECT DISTINCT(src) FROM packets WHERE src NOT LIKE $1',
      values: ['192.168.0.%'],
    };

    const { rows } = await db.query(query);
    return rows.map((row) => row.src);
  } catch (error) {
    console.error(error);
  }
}

async function getGeoIps() {
  try {
    const ips = await getSrcIps();
    console.log(ips);
    const {
      data,
    } = await axios.post(
      'http://ip-api.com/batch?fields=country,region,city,lat,lon,isp,org,as,query',
      { ips },
    );
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

subscriber.on('message', function (channel, message) {
  if (channel === 'packets') {
    const packet = JSON.parse(message);
    insertPacket(packet);
    // console.log(packet);
  }
});

setInterval(() => {
  getGeoIps();
}, 5000);

subscriber.subscribe('packets');
