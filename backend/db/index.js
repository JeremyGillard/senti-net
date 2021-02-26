const { Pool } = require('pg');

const pool = new Pool({
  user: 'sentinet',
  host: 'localhost',
  database: 'sentinet',
  password: 'sentinet',
  port: 5432,
});

module.exports = {
  query: (text, params, callback) => {
    return pool.query(text, params, callback);
  },
};
