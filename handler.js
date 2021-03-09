const gif = require("./commands/gif.js")
const play = require("./commands/play.js")
const status = require("./commands/status.js")
const leave = require("./commands/leave.js")

const commands = {play, gif, status, leave};

module.exports = async function (msg) {
    let args = msg.content.split(" ");
    let command = args.shift();
    if (command.charAt(0) === '!') {
        command = command.substring(1);
        console.log('Command: ' + command);
        console.log('Args: ' + args);
        commands[command](msg, args.toString());
    }
}