module.exports = function (msg) {
    console.log("Sending gif");
    switch (msg.content) {
        case '!pug':
            msg.channel.send('https://media.giphy.com/media/ZX63w9xm4ilgs/giphy.gif');
            break;
        case '!hehe':
            msg.channel.send('https://media.giphy.com/media/dPEJxh06y4OTC/giphy.gif');
            break;
        case '!noice':
            msg.channel.send('https://media.giphy.com/media/yJFeycRK2DB4c/giphy.gif');
            break;
        case '!пиздец':
            msg.channel.send('https://media.giphy.com/media/Zqe1S3qNQxsuQ/giphy.gif');
            break;
        case '!wiggle':
            msg.channel.send('https://media.giphy.com/media/b3Gp6a25caNZC/giphy.gif');
            break;
        default:
            console.log('No such gif');
            break;
    }
}