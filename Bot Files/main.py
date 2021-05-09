from keep_alive import keep_alive
import discord
import os
import random
import requests
import json
from randfacts import getFact
from discord.utils import find


client = discord.Client()
print('Hello, World')

coin_stuff = ['You got Heads!', 'You got Tails!']

random = random.choice(coin_stuff)

@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        embed = discord.Embed(title="Hello!", description="Hello! I am very glad you added me to **"+"{}".format(guild.name)+"**! Thanks for that! If you want to support us, please vote us in top.gg. https://top.gg/bot/809002048447184948/vote", color=0x1abc9c)
        await general.send(embed=embed)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

@client.event
async def on_ready():
    await client.change_presence( activity=discord.Activity( type=discord.ActivityType.competing, name='Pokemon Battles'))
    print('{0.user} is ready!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('r!help'):
        await message.add_reaction('👌')
        embedVar = discord.Embed(title="Commands", description="All of Registeel's Commands!", color=0x1abc9c)
        embedVar.add_field(name='Fun Commands', value='`r!help fun`', inline=True)
        embedVar.add_field(name='Games', value='`r!help games`', inline=False)
        embedVar.add_field(name='Other commands', value='`r!help other`', inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('r!help fun'):
        embedVar = discord.Embed(title="FUN Commands", description="`r!randomnumber, r!yt, r!say <message>, r!poll, r!fact`", color=0x1abc9c)
        embedVar.add_field(name="Go to: 7 Wonders of The World", value="`r!goto taj mahal, r!goto colosseum, r!goto chichen itza, r!goto machu picchu, r!goto Christ the Redeemer, r!goto petra, r!goto great wall of china`")
        await message.channel.send(embed=embedVar)

    if message.content == ('r!help games'):
        embedVar= discord.Embed(title="Games", description="Game Commands", color=0x1abc9c)
        embedVar.add_field(name="Simple Games", value="`r!coinflip`", inline=False)
        embedVar.add_field(name="Economy", value="*Coming Soon*", inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ('r!help other'):
        embedVar= discord.Embed(title="Other Commands", description="`r!quote, r!sourcecode, r!website, r!invite, r!vote, r!help`", color=0x1abc9c)
        await message.channel.send(embed=embedVar)

    if message.content == ('r!quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content == ('r!invite'):
        await message.channel.send(
            'https://discord.com/api/oauth2/authorize?client_id=809002048447184948&permissions=8&scope=bot'
        )

    if message.content == ('r!website'):
        await message.channel.send(
            'https://sites.google.com/view/registeeldiscordbot')

    if message.content == ('r!yt'):
        await message.channel.send('Subscribe here! https://www.youtube.com/channel/UCxzkAP7o94jO-5U1DcESA8w')

    if message.content == ('r!randomnumber'):
      randomnumber = random.randint(0,1000)
      await message.channel.send(randomnumber)
      if randomnumber == 626:
        await message.channel.send('Your number is **626**. You win a cookie :)')

    if message.content == ('r!sourcecode'):
        await message.channel.send(
            'https://github.com/theultimatepokemontrainer/registeeldiscordbot'
        )

    if message.content == ('r!coinflip'):
        embedVar = discord.Embed(title="Coin Flipped!", description=random, color=0xf1c40f,)
        await message.channel.send(embed=embedVar)

    if message.content == ('r!vote'):
        await message.channel.send('You can vote every 12 hours! https://top.gg/bot/809002048447184948/vote')

    if message.content == ('r!poll'):
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.channel.send('👍 for yes 👎 for no')

    if message.content == ("r!say"):
        await message.channel.send(message.content[5:].format(message))

    if message.content == ('r!fact'):
        x = getFact()
        embed = discord.Embed(title='{}, here is your fact'.format(message.author.name), description=x, color=0x1abc9c)
        await message.channel.send(embed=embed)

    if message.content == ("r!goto taj mahal"):
        await message.channel.send('https://cdn.britannica.com/86/170586-050-AB7FEFAE/Taj-Mahal-Agra-India.jpg')

    if message.content == ("r!goto colosseum"):
        await message.channel.send('https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/250px-Colosseo_2020.jpg')

    if message.content == ("r!goto chichen itza"):
        await message.channel.send('https://cdn.hswstatic.com/gif/chichen-itza.jpg')

    if message.content == ("r!goto machu picchu"):
        await message.channel.send('https://i.guim.co.uk/img/media/b56952349419f749667d43f38b4d05e2980821a2/0_176_6016_3611/master/6016.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=d1d59c0c9b0e70e1da5989902cf5f01c')    

    if message.content == ("r!goto Christ the Redeemer"):
        await message.channel.send('http://4.bp.blogspot.com/-yA1inFreZAQ/Uei0hFMHFsI/AAAAAAAAHMY/rTic90zSDmk/s1600/BrasilCorcovadoStatue.jpg')

    if message.content == ("r!goto petra"):
        await message.channel.send('https://travelsquire.com/ts/wp-content/uploads/2019/10/Petra-Feature.jpg')

    if message.content == ("r!goto great wall of china"):
        await message.channel.send('https://cdn.getyourguide.com/img/location/5457947b8a235.jpeg/92.jpg')

keep_alive()
client.run(os.getenv('TOKEN'))
