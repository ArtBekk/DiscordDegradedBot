const gif = require ("./commands/gif.js")
const ytPlayer = require("./commands/ytPlayer.js")

module.exports = async function (msg) {
    if (msg.guild.id === '336199770185924608')
    {
        switch (msg.content)
        {
            case '!play':
                console.log('Music request');
                //TODO implement player from youtube
                break;
            default:
                console.log('Gif request');
                gif(msg);
        }
    }
}