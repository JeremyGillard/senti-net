const redis = require("redis");

const subscriber = redis.createClient();

subscriber.on("message", function (channel, message) {
  if (channel === "packets") {
    const packet = JSON.parse(message);
    console.log(packet);
  }
});

subscriber.subscribe("packets");
