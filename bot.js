const Discord = require('discord.js');
require("dotenv").config();

const handler = require('./handler.js');

const client = new Discord.Client();
client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}, u dev-ass`);
});

client.login(process.env.TOKEN);

client.on("message", handler);