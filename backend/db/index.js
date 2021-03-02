const { Pool } = require('pg');

const pool = new Pool({
  user: 'sentinet',
  host: 'localhost',
  database: 'sentinet',
  password: 'sentinet',
  port: 5432,
});

async function insertPacket(packet) {
  try {
    const query = {
      text:
        'INSERT INTO packets (capture_datetime, src, sport, dst, dport, proto) VALUES ($1, $2, $3, $4, $5, $6)',
      values: Object.values(packet),
    };

    await pool.query(query);
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
    // const {
    //   data,
    // } = await axios.post(
    //   'http://ip-api.com/batch?fields=country,region,city,lat,lon,isp,org,as,query',
    //   { ips },
    // );
    // console.log(data);
  } catch (error) {
    console.error(error);
  }
}

module.exports = {
  insertPacket: insertPacket,
  getSrcIps: getSrcIps,
  getGeoIps: getGeoIps,
};
