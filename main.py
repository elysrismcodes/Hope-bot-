import discord
from discord.ext import commands
import nacl
import keep_alive
import asyncio
import os

intents = discord.Intents.all()
emcolour = 0xB465FE
hope = "<:Hope:1064963520317378560>"

client = commands.Bot(command_prefix="h!",
                      intents=intents,
                      activity=discord.Streaming(
                          name="@HopeEsportsGG on twitter!",
                          url="https://twitch.tv/HopeUprises/"))


@client.event
async def on_ready():
    print(f"{client.user.name} is ready")
    channel = client.get_channel(1064960492696776815)
    await channel.connect()


import sys


def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)


@client.command(aliases=['res'])
async def restart(ctx):
    id = str(ctx.author.id)
    if id == '998711126097395813':
        await ctx.reply(
            "I love how you turn me off, and then turn me on so fast🥵")
        restart_bot()
    else:
        await ctx.reply("You do not have the permissions to use this command!")


@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title=f"Welcome To Assure!",
        description=
        f"Hey {member.mention}, Welcome to the Assure community discord server!, head <#1061691312681791561> to See how To Join Hope, and make sure to check out <#1061691305404665946>!",
        color=emcolour)
    embed.add_field(name="Membercount", value=f"`{member.guild.member_count}`")
    embed.set_image(
        url=
        "https://media.discordapp.net/attachments/1066464238731792504/1067530314441838642/header.png?width=1440&height=480"
    )
    await client.get_channel(1061691320281866240).send(embed=embed)

@client.command()
async def ping(ctx):
    print(f"{ctx.author} used the ping command")
    embed = discord.Embed(
        title="Pong!",
        description=
        f"**My ping is `{round(client.latency * 1000)}`ms** <:Hope:1064963520317378560>",
        color=emcolour)
    embed.set_footer(text=f"Invoked by {ctx.author}",
                     icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def socials(ctx):
    print(f"{ctx.author} used the socials command")
    embed = discord.Embed(
        title="Hope Socials",
        description="Keep up to date with hope.",
        color=emcolour)
    embed.add_field(name="Twitter",
                    value="[Hope Twitter](https://twitter.com/TeamHopeGGs)",
                    inline=False)
    embed.add_field(
        name="Instagram",
        value=
        "[Hope Instagram](https://www.instagram.com/teamhopeggs/)",
        inline=False)
    embed.add_field(
        name="YouTube",
        value=
        "[Hope YouTube](https://www.youtube.com/@TeamHopeGGs/videos)",
        inline=False)
    embed.set_image(
        url=
        "https://pbs.twimg.com/profile_banners/1565134437678886912/1673205407/1500x500"
    )
    embed.set_footer(text=f"Invoked by {ctx.author}")
    await ctx.send(embed=embed)


@client.command(aliases=["mc"])
async def membercount(ctx):
    print(f"{ctx.author} used the membercount command")
    embed = discord.Embed(
        title="Hope Membercount",
        description=f"**Hope has `{ctx.guild.member_count}` members **",
        color=emcolour)
    embed.set_footer(text=f"Invoked by {ctx.author}",
                     icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command(aliases=["av"])
async def avatar(ctx, member: discord.Member = None):
    print(f"{ctx.author} used the av command")
    if member == None:
        member = ctx.author
        embed = discord.Embed(
            title=f"{member}'s avatar {hope}",
            description=f"[Click To Open]({member.avatar_url})",
            color=emcolour)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"Invoked by {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f"{member}'s avatar {hope}",
            description=f"[Click To Open]({member.avatar_url})",
            color=emcolour)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"Invoked by {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


@client.command(aliases=["echo, repeat"])
async def say(ctx, *, arg):
    print(f"{ctx.author} used the say command")
    await ctx.message.delete()
    await ctx.send(f"{arg} - {ctx.author}")


@client.command(aliases=["message", "msg"])
@commands.has_permissions(manage_messages=True)
async def dm(ctx, member: discord.Member, *, arg):
    print(f"{ctx.author} used dm command")
    await ctx.message.delete()
    await member.send(f"{arg} - {ctx.author}")


snipe_message_author = {}
snipe_message_content = {}


@client.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    await asyncio.sleep(60)
    del snipe_message_author[message.channel.id]
    del snipe_message_content[message.channel.id]


@client.command(aliases=['s'])
async def snipe(ctx):
    print(f"{ctx.author} used snipe command")
    channel = ctx.channel
    try:
        embed = discord.Embed(
            title=f"Last deleted message in #{channel.name} {hope}",
            description=
            f"**{snipe_message_content[channel.id]} - {snipe_message_author[channel.id]}**",
            color=emcolour)
        embed.set_footer(text=f"Invoked by {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    except KeyError:
        embed = discord.Embed(title='Error',
                              description='There is nothing to snipe.')
        await ctx.reply(embed=embed)


client.run(os.getenv("TOKEN"))
