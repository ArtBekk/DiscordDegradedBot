const ytdl = require('ytdl-core');
const ytSearch = require('yt-search');

module.exports = async function (msg, args) {
    const request = args.join(' ');
    const voiceChannel = msg.member.voice.channel;

    if (!voiceChannel) msg.reply("You'd better get your ass in some voice channel before asking me that, fam");

    if (!request.length) msg.reply("Don't spam commands without actually telling me what to do idiot");

    const validURL = (str) => {
        var regex = /(http|https):\/\/(\w+:{0,1}\w*)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%!\-\/]))?/;
        if (!regex.test(str)) {
            return false;
        } else {
            return true;
        }
    }

    if (validURL(request)) {

        const connection = await voiceChannel.join();
        const stream = ytdl(request, {filter: 'audioonly'});

        connection.play(stream, {seek: 0, volume: 1})
            .on('finish', () => {
                voiceChannel.leave();
                msg.channel.send('Your taste sucks, never call me again');
            });

        await message.reply(`Playing from link ${request} or whatever`)

        return
    }

    const connection = await voiceChannel.join();
    const videoFinder = async (query) => {
        const videoResult = await ytSearch(query);
        return (videoResult.videos.length > 1) ? videoResult.videos[0] : null;
    }

    const video = await videoFinder(request);

    if (video) {
        const stream = ytdl(video.url, {filter: "audioonly"});
        connection.play(stream, {seek: 0, volume: 1})
            .on('finish', () => {
                voiceChannel.leave();
                msg.channel.send('Your taste sucks, never call me again');
            });
        await msg.reply(`Playing some "${request}" or whatever`);
    }
}