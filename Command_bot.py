import discord
from dotenv import load_dotenv
import os
import emojis
import time
import asyncio
import random
from discord.utils import get
from discord.ext import commands
from discord_slash.utils import manage_commands
from discord_slash import SlashCommand

guild_ids = [398872615298531328, 705828780756697148, 840616780836634655]

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

load_dotenv()
TOKEN = os.getenv(
    'DISCORD_TOKEN')

colors = discord.Color
poll_color = colors.blurple()


helpme = discord.Game("*poll.helpme/*poll.helpus")

poll_help = discord.Embed(
    description='This help message.\n\n```\n*poll "{time}" "{title}" "(emoji 1){option 1}" "(emoji 2){option 2}" "(emoji n){option n}"\n\nExample:\n*poll "120" "This is a title" "👌 Option 1" "👍🏻 Option 2"```You can use n number of options. \n\n ```/gaali @user``` Gives Gaali to mentioned user \n\n Thanks', color=poll_color)

poll_error = discord.Embed(description="It seems like there was an error processing this. Please check again that you have formatted the message correctly. Sadly, this bot is dumb so unless the message is formatted correctly it will not be understood. If you need any help formatting please send ``*poll.helpme`` or ``*poll.helpus``. If there are any more issues fell free to join the support discord, which isn't actully a thing yet...sry.", color=colors.red())


invite_link = 'https://discord.com/api/oauth2/authorize?client_id=795267848883798017&permissions=1208351808&scope=bot'

img1 = 'https://cdn.discordapp.com/attachments/852955340681117737/852955620327424060/Screenshot_20210611-083503_Discord.jpg'

rani = "https://cdn.discordapp.com/attachments/845574281681174538/853362687344640020/60c511b9d8cc9023121327.gif"

poll = ""
creator = ""
polluser = ""
t1 = 0


@slash.slash(
    name="gaali",
    description="Abuse Someone",
    options=[manage_commands.create_option(
        name="person",
        description="Tag the person to abuse",
        option_type=3,
        required=True,
    ),
    ],

    guild_ids=guild_ids
)
async def _test(ctx, person: str):
    print(person)
    # await ctx.respond(hide=True)
    polluser1 = str(ctx.author.id)
    if(person == "<@!307120290905849869>"):

        member2 = "<@"+polluser1+">"
        resp = f"{member2} You cant give gaali to <@!307120290905849869>"
        await ctx.send(resp)
    elif(person == "<@!795267848883798017>" or person == "<@795267848883798017>"):

        member2 = "<@"+polluser1+">"
        list2 = [
            f"saale apne baap ko gaali dega {member2}?",
            f"tu rahine de randibaaz {member2}",
            f"{member2} tu kya gaali dega re mere ko?",
            f"chup bahit lavde {member2}"
        ]
        resp = random.choice(list2)
        await ctx.send(resp)
    else:
        gaali1 = [
            f"chinaal {person}",
            f"haraami {person}",
            f"{person} najayaz",
            f"sale {person} tatti",
            f"{person} tu betichod hai",
            f"jhaantu {person}",
            f"ullu {person}",
            f"chodu {person}",
            f"abe {person} lund",
            f"bc chuttad {person}",
            f"bakrichod {person}",
            f"sale {person} randibaaz",
            f"bhosadchod {person}",
            f"jhaant chaatu {person}",
            f"mayawati ki gaand sale {person}",
            f"{person} chut pakoda",
            f"{person} gadhe ki paad",
            f"chodu bhagat {person}",
            f"{person} sadi hui gaand",
            f"{person} tu Lund fakir hai!",
            f"baawli gand {person}",
            f"abe {person} bagal ke baal",
            f"are {person} chaman chutiye tu rahine de!",
            f"{person} kaali Chut Ke Safed Jhaant",
            f"lund Ke pasine mein tala hua bhajiya hai tu {person}",
            f"{person} lode jaisi shakal hai teri!",
            f"tere gaand me kuch jyada hi keede hai {person}",
            f"{person} lamde tu chup baith",
            f"chup baith {person}, varna tere gaand me jhadu dal ke moor bana dunga",
            f"{person} aisa lavda fek ke maarunga na ki tu apna naam bhul jayega",
            f"bhosadpappu {person}",
            f"{person} chup bas nahi tr asa maren ki gotya kapalat jatil!",
            f"{person} gaand faad dunga!",
            f"jhant ke jhinguur {person}",
            f"{person} bhadwe tere gand me sulemani keeda dalunga",
            f"saale machhar ki jhaant {person}",
            f"{person} gaandu madarchod mkc teri",
            f"chodumpatti {person}",
            f"{person} chup kar bsdk nahi to lund par ghunghru pehen ke chodunga lagega kirtan chal raha hai",
        ]
    x = random.choice(gaali1)
    await ctx.send(x)


def parse_poll(message):
    global t1
    poll = message.content.split('"')
    poll_options = ""
    emoji = iter('🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿'.split())
    emoji_opt = []
    i = 1
    t1 = int(poll[1])
    del poll[1]
    del poll[1]
    del poll[0]
    poll[0] = poll[0].strip()
    poll_title = "**:bar_chart: " + str(poll[0]) + "**"
    while i < len(poll)-1:
        del poll[i]
        poll[i] = poll[i].strip()
        if poll[i].startswith("<"):
            poll_options = poll_options + poll[i] + "\n"
            emoji_opt.append(poll[i].split(">")[0])
            emoji_opt[-1] = emoji_opt[-1] + ">"
        elif emojis.get(poll[i][0]) != set():
            poll_options = poll_options + poll[i] + "\n"
            emoji_opt.append(emojis.get(poll[i][0]).pop())
        else:
            current_emoji = next(emoji)
            poll_options = poll_options + current_emoji + ' ' + poll[i] + '\n'
            emoji_opt.append(current_emoji)
        i += 1
    print(poll_options)
    poll_options = discord.Embed(description=poll_options, color=poll_color)
    poll = [poll_title, poll_options, emoji_opt]
    return poll


@client.event
async def on_ready():
    print("Online!")
    await client.change_presence(activity=discord.Game('Listening for *poll.help'))


@client.event
async def on_message(message):
    global poll
    global polluser
    if message.author != client.user:
        if message.content.startswith('*poll.helpme'):
            await message.channel.send(content='**poll.help**', embed=poll_help)
            await message.delete()
        elif message.content.startswith('*poll.help'):
            await message.channel.send(content='**poll.help**', embed=poll_help)
            await message.delete()
        elif message.content.startswith('*poll.helpus'):
            await message.channel.send(content='**poll.help**', embed=poll_help)
            await message.delete()
        elif message.content.startswith('*poll.invite'):
            await message.channel.send(invite_link)
            await message.delete()
        elif message.content.startswith('!jinnelert'):
            await message.channel.send(img1)
        elif message.content.startswith('!rani'):
            await message.channel.send(rani)
        elif message.content.startswith("*poll"):
            try:
                poll = parse_poll(message)
            except:
                poll = [
                    '**ERROR**', discord.Embed(description=poll_error, color=colors.red()), ]
                await creator.send(message)
                await creator.send(message.content)
            polluser = str(message.author.id)
            print(polluser)
            await message.delete()
            await message.channel.send(content=poll[0], embed=poll[1])
    if message.author == client.user and message.content.startswith('**:bar_chart:'):
        for emoji in poll[2]:
            await message.add_reaction(emoji)
        print(t1)
        await asyncio.sleep(t1)
        # *poll "60" "test" "yes" "no"
        rec = {}
        res = """**Result is:**\n"""
        for each in poll[2][:]:
            reac = get(message.reactions, emoji=each)
            rec[each] = reac.count
        maxx = max(rec, key=rec.get)
        for k, v in rec.items():
            res = res + str(k) + "  :  " + "**"+str(v)+"**" + "\n"
        member1 = "<@"+polluser+">"
        poll_result = discord.Embed(description=res, color=poll_color)
        await message.channel.send(content=member1, embed=poll_result)
    if message.author != client.user:
        if client.user.mentioned_in(message):
            per1 = str(message.author.id)
            per2 = "<@"+per1+">"
            list2 = [
                f"are lavde mere ko kyu tag kiya? {per2}?",
                f"phirse tag kiya to gand fod dunga {per2}",
                f"{per2} tere ko kuch kam dhanda nahi hai kya bc?",
                f"apne baap ko kyu tag kia? {per2}"
            ]
            resp = random.choice(list2)
            await message.channel.send(resp)
    # await client.process_commands(message)


client.run(TOKEN)
