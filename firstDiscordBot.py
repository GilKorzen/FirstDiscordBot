
import os
import random
from discord.utils import get
import discord
from dotenv import load_dotenv


dic = {}
list_forbidden_words=['''ADD HERE WORDS/SENTENCES YOU WANT TO BAN''']

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    print("fuck")
    await member.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    if message.content == "yes":
        channel = client.get_channel('''censored ID''') #Add an ID of a secret room
        try:
            await message.author.move_to(channel)
            await message.delete()
        except:
            print("knew this was gonna happen")
    try:
        if message.author.id != '''censored ID''': #Add an ID of a member who you want to make immune from muting
            if not (str(message.author) in dic):
                dic[str(message.author)] = [message.content, 0]
            elif dic[str(message.author)][0] == message.content:
                dic[str(message.author)][1] += 1
                if dic[str(message.author)][1] == 2:
                    await message.channel.send(message.author.mention + " STOP")
                elif dic[str(message.author)][1] == 4:
                    await message.channel.send(message.author.mention + " SHUT UP")
                    role = get(message.author.guild.roles, name="muted")
                    for roleee in message.author.roles[1:]:
                        if roleee.name != "DJ":
                            await message.author.remove_roles(roleee)
                    await message.author.add_roles(role)
            elif dic[str(message.author)][0] != message.content:
                dic[str(message.author)][0] = message.content
                dic[str(message.author)][1] = 0
    except:
        print("")

    if message.author == client.user:
        return
    if message.content == "!movit": #use it to troll one of your friends, this commands moves one specific member to an abandoned room

        for mem in client.get_all_members():
            if mem.id == '''censored ID''': #Add an ID
                member = mem
        channel = client.get_channel('''censored ID''') #Add an ID
        try:
            await member.move_to(channel)
        except:
            print("knew this was gonna happen")

    elif message.content == "GOAT":
        channel = client.get_channel('''censored ID''')
        await channel.send("!p gustavo lima balada")

    elif message.content.startswith("!mute") and len(message.content.split(" ")) == 2:
        print(message.content.split(" ")[1][3:-1])
        members = client.get_all_members()
        for mem in members:
            if mem.id == int(message.content.split(" ")[1][3:-1]):
                gotcha = mem
        role = get(gotcha.guild.roles, name="muted")
        for roleee in gotcha.roles[1:]:
            if roleee.name != "DJ":
                await gotcha.remove_roles(roleee)
        await gotcha.add_roles(role)

    elif message.content.startswith("spam") and (
            message.author.id == '''censored id''' or message.author.id == '''censored id'''):
        new_message = ""
        for letter in message.content:
            if letter == '"':
                break
            else:
                new_message += letter
        message_splitter = new_message.split(' ')
        message_to_deliver = message.content[len(new_message) + 1:-1]
        print(message_splitter)
        me = int(message_splitter[1][3:-1])
        sorry = client.get_user(me)
        for a in range(int(message_splitter[2])):
            try:
                await sorry.send(message_to_deliver)
                print(message_to_deliver)
            except:
                print("oh no")
        await message.delete()
    elif message.content == "!p שרת ביוני":
        await message.channel.send(message.author.mention + " קראת לי? ")
        await message.channel.send(message.author.mention + " answer with yes ")
    elif any(word.lower() in str(message.content).lower() for word in list_forbidden_words):
        try:
            await message.author.send("That's not nice")
        finally:
            await  message.delete()
            await message.guild.kick(message.author)
            await message.channel.send(str(message.author) + " was kicked due to violation of the rules")
    elif message.content == "I won't violate any rule" and message.author.id != '''censored ID''': #Add an ID
        member = message.author
        role = get(member.guild.roles, name="צדיקים")
        await member.add_roles(role)
    elif message.content == "!roles" or message.content == "!role":
        await message.channel.send("if you want to have a role please type: I won't violate any rule")

    elif 'https://discord.gg/' in message.content: #Prevents self promotion
        await message.delete()
    if '''insert name''' in message.content.lower() or '''insert more names if you want to''' in message.content:
        await message.channel.send(message.author.mention + "hope you said something good about him ")


client.run(TOKEN)
