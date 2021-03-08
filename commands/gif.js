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
        case 'smugwink':
            msg.channel.send('https://media.giphy.com/media/wkW0maGDN1eSc/giphy.gif');
            break;
        case 'kawaii':
            msg.channel.send('https://media.giphy.com/media/anDhBXwgvIa7m/giphy.gif');
            break;
        case 'eh?':
            msg.channel.send('https://media.giphy.com/media/3o7btMCltyDvSgF92E/giphy.gif');
            break;
        case 'владыка':
            msg.channel.send('https://media.giphy.com/media/Mfq2ko7m1eMaQ/giphy.gif');
            break;
        case 'derpmeow':
            msg.channel.send('https://tenor.com/view/cat-meow-big-lips-gif-13233291');
            break;
        case 'че бля' || 'чебля' || 'чёбля' || 'чё бля' :
            msg.channel.send('https://tenor.com/view/buff-pikachu-strong-muscle-pokemon-gif-15308559');
            break;
        case 'насука' || 'нассука' || 'на сука' || 'на ссука' :
            msg.channel.send('https://tenor.com/view/anime-gif-9509158');
            break;
        case 'дя' :
            msg.channel.send('https://tenor.com/view/anime-sparkle-happy-gif-6014346');
            break;
        case 'бля' :
            msg.channel.send('https://tenor.com/view/blends-anime-maika-gif-10176024');
            break;
        case 'nom' || 'жрать' :
            msg.channel.send('https://tenor.com/view/eat-crab-anime-loli-dragon-gif-9920851');
            break;
        case 'ня' :
            msg.channel.send('https://tenor.com/view/anime-cat-cute-gif-16038419');
            break;
        case 'батя' :
            msg.channel.send('https://tenor.com/view/norogami-anime-slide-gif-4697082');
            break;
        default:
            let url = `https://api.tenor.com/v1/search?q=${keywords}&key=${process.env.TENOR_KEY}`;
            let response = await fetch(url);
            let json = await response.json();
            const index = Math.floor(Math.random() * json.results.length);
            msg.channel.send(json.results[index].url);
    }
}