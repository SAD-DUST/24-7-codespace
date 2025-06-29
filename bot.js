const mineflayer = require('mineflayer');

const bot = mineflayer.createBot({
  host: '148.113.216.61', // e.g., 'localhost' or 'mc.hypixel.net'
  port: 3162,            // Minecraft default port
  username: 'VIP_ChunkLoader',    // Use email if it's an online-mode server
  version: false          // false = auto-detect
});

bot.on('spawn', () => {
  console.log('Bot has spawned! Staying AFK.');

  // Optional: Make the bot jump periodically to prevent AFK kick
  setInterval(() => {
    bot.setControlState('jump', true);
    setTimeout(() => bot.setControlState('jump', false), 500);
  }, 10000); // Every 10 seconds

  // Optional: Random look to mimic player movement
  setInterval(() => {
    const yaw = Math.random() * Math.PI * 2;
    const pitch = (Math.random() - 0.5) * Math.PI;
    bot.look(yaw, pitch, true);
  }, 15000);
});

bot.on('end', () => {
  console.log('Bot disconnected. Reconnecting...');
  setTimeout(() => process.exit(1), 5000); // Exit for pm2 or a script to restart
});

bot.on('error', err => console.log('Error:', err));
