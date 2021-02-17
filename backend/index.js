const redis = require("redis");

const subscriber = redis.createClient();

subscriber.on("message", function (channel, message) {
  if (channel === "packets") {
    console.log(JSON.parse(message));
  }
});

subscriber.subscribe("packets");
