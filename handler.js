const gif = require("./commands/gif.js")
const ytPlayer = require("./commands/ytPlayer.js")
const status = require("./commands/status.js")

const commands = {ytPlayer, gif, status};

module.exports = async function (msg) {
    console.log('Handling a command')
    let args = msg.content.split(" ");
    let command = args.shift();
    if (command.charAt(0) === '!') {
        command = command.substring(1);
        console.log('Command: ' + command);
        console.log('Args: ' + args);
        commands[command](msg, args.toString());
    }
}