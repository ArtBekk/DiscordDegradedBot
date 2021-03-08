const gif = require("./commands/gif.js")
const ytPlayer = require("./commands/ytPlayer.js")
const status = require("./commands/status.js")

const commands = {ytPlayer, gif, status};

module.exports = async function (msg) {
    let args = msg.content.split(" ");
    let command = args.shift().toString();
    if (command.charAt(0) === '!') {
        command = command.substring(1);
        commands[command](msg, args);
    }
}