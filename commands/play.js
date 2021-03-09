const ytdl = require('ytdl-core');
const ytSearch = require('yt-search');

module.exports = async function (msg, args) {
    const voiceChannel = msg.member.voice.channel;

    if (!voiceChannel) msg.reply("You'd better get your ass in some voice channel before asking me that, fam");

    if (!args.length) msg.reply("Don't spam commands without actually telling me what to do idiot");

    const connection = await voiceChannel.join();
    const videoFinder = async (query) => {
        const videoResult = await ytSearch(query);
        return (videoResult.videos.length > 1) ? videoResult.videos[0] : null;
    }

    const video = await videoFinder(args);

    if (video) {
        const stream = ytdl(video.url, {filter: "audioonly"});
        connection.play(stream, {seek: 0, volume: 1})
            .on('finish', () => {
                voiceChannel.leave();
            });
    }
}