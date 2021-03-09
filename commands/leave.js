module.exports = async function (msg, args) {
    const voiceChannel = msg.member.voice.channel;
    if (!voiceChannel) msg.reply("You'd better get your ass in some voice channel before asking me that, fam");
    await voiceChannel.leave();
    await msg.channel.send('Your taste sucks, never call me again');
}