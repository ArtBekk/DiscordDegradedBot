const fetch = require('node-fetch');

module.exports = async function (msg, keywords) {
    console.log("Sending gif");
    switch (keywords) {
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
            const url = `https://api.tenor.com/v1/search?q=${keywords}&key=${process.env.TENOR_KEY}`;
            const response = await fetch(url);
            const result = await response.json();
            const index = await Math.floor(Math.random() * result.results.length);
            await msg.channel.send(result.results[index].url);
            break;
    }
}