const fetch = require("node-fetch");

module.exports = function (msg, args) {
    console.log("Sending gif");
    switch (args) {
        case 'pug':
            msg.channel.send('https://media.giphy.com/media/ZX63w9xm4ilgs/giphy.gif');
            break;
        case 'hehe':
            msg.channel.send('https://media.giphy.com/media/dPEJxh06y4OTC/giphy.gif');
            break;
        case 'noice':
            msg.channel.send('https://media.giphy.com/media/yJFeycRK2DB4c/giphy.gif');
            break;
        case 'пиздец':
            msg.channel.send('https://media.giphy.com/media/Zqe1S3qNQxsuQ/giphy.gif');
            break;
        case 'wiggle':
            msg.channel.send('https://media.giphy.com/media/b3Gp6a25caNZC/giphy.gif');
            break;
        default:
            console.log('Making a request for random gif from Tenor')
            let keywords;
            if (args.length > 0) {
                keywords = args.join(" ");
            }
            let url = `https://api.tenor.com/v1/search?q=${keywords}&key=${process.env.TENORKEY}`;
            let response = await fetch(url);
            let json = await response.json();
            const index = Math.floor(Math.random() * json.results.length);
            msg.channel.send(json.results[index].url);
            break;
    }
}