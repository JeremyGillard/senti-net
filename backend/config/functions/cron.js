"use strict";

/**
 * Cron config that gives you an opportunity
 * to run scheduled jobs.
 *
 * The cron format consists of:
 * [SECOND (optional)] [MINUTE] [HOUR] [DAY OF MONTH] [MONTH OF YEAR] [DAY OF WEEK]
 *
 * See more details here: https://strapi.io/documentation/developer-docs/latest/concepts/configurations.html#cron-tasks
 */

module.exports = {
  /**
   * Simple example.
   * Every monday at 1am.
   */
  // '0 1 * * 1': () => {
  //
  // }
  "43 * * * *": async () => {
    try {
      console.log("UPDATE!");
      // fetch packets to publish
      const draftPacketsToPublish = await strapi.api.packets.services.packets.find(
        { _limit: -1 }
      );

      console.log(draftPacketsToPublish.length);
      // update published_at of packets
      draftPacketsToPublish.forEach(async (packet) => {
        await strapi.api.packets.services.packets.update(
          { id: packet.id },
          { published_at: new Date() }
        );
      });
    } catch (error) {
      console.log(error);
    }
  },
};
