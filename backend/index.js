const redis = require("redis");

const subscriber = redis.createClient();

subscriber.on("message", function (channel, message) {
  console.log({ channel });
  console.log({ message });
});

subscriber.subscribe("packets");
