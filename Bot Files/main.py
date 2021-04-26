from keep_alive import keep_alive
import discord
import os
import random
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands
import pokebase as pb

load_dotenv()
client = discord.Client()
print('Hello, World')

pokemon_words = [
    "I want to be a pokemon master!", "Let's Go!", "Pikachu use Thunderbolt!",
    "YEAH!", "Pokemon!"
]

pokemon_responses = [
    "Cool!", "I like your spirit!", "You are a great person / bot!",
    "Do you know Mega Evolution?"
]

igot_caught = ["You have caught the wild Registeel"]

mining_stuff = ["You mined Stone!", "You mined Dirt...","You mined DIAMONDS", "You mined Emerald", "You mined nothing LOL", "You mined Redstone, cool!", "You mined GOLD"]

pkmnto_catch = ['You caught a Pikachu', 'You caught a Zebstrika', 'You caught a Lugia', 'You caught a Venusaur', 'You caught an ARCEUS OMG', 'You caught a Snom. EEEE', 'You caught..... Nothing']

coin_stuff = ['You got Heads!', 'You got Tails!']

random = random.choice(coin_stuff)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    await client.change_presence( activity=discord.Activity(status=discord.Status.dnd, type=discord.ActivityType.competing, name='r!help'))
    print('{0.user} is ready!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('r!help'):
        await message.add_reaction('👌')
        embedVar = discord.Embed(title="Commands", description="All of Registeel's Commands!", color=323233)
        embedVar.add_field(name='Fun Commands', value='```r!fun```', inline=True)
        embedVar.add_field(name='Important Commands', value='```r!important```', inline=True)
        embedVar.add_field(name='Games', value='```r!games```', inline=True)
        embedVar.add_field(name='Other commands', value='```r!other```', inline=True)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('r!fun'):
        embedVar = discord.Embed(title="FUN Commands", description="```r!rickroll, r!pingeveryone, r!registeelheight, r!registeelweight, r!registeelsprite, r!gimmeameem, r!amongus, r!randomnumber, r!yt, r!say <message>, r!poll```", color=323233)
        embedVar.add_field(name='Shrek', value='```r!shrek, r!donkey```')
        await message.channel.send(embed=embedVar)

    if message.content.startswith('r!important'):
        embedVar= discord.Embed(title="Important commands", description="```r!vote, r!help```", color=323233)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('r!games'):
        embedVar= discord.Embed(title="Games", description="Game Commands", color=323233)
        embedVar.add_field(name="Simple Games", value="```r!coinflip```", inline=False)
        embedVar.add_field(name="Economy", value="*Coming Soon*", inline=False)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('r!other'):
        embedVar= discord.Embed(title="Other Commands", description="```r!randomquote, r!hello, r!goodbye, r!creator, r!sourcecode, r!website, r!invite```", color=323233)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('r!randomquote'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in message.content for word in pokemon_words):
       await message.channel.send(random.choice(pokemon_responses))

    if message.content.startswith('r!hello'):
        await message.channel.send('Hello')

    if message.content.startswith('r!goodbye'):
        await message.channel.send('Bye. Hope you had a great time!')

    if message.content.startswith('r!invite'):
        await message.channel.send(
            'https://discord.com/api/oauth2/authorize?client_id=809002048447184948&permissions=8&scope=bot'
        )

    if message.content.startswith('r!rickroll'):
        await message.add_reaction('🐸')
        await message.channel.send(
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    if message.content.startswith('r!pingeveryone'):
        await message.channel.send('Hello @everyone!')


    if message.content.startswith('r!registeelheight'):
        registeel = pb.pokemon('registeel')
        await message.channel.send(registeel.height)

    if message.content.startswith('r!registeelweight'):
        registeel = pb.pokemon('registeel')
        await message.channel.send(registeel.weight)

    if message.content.startswith('r!registeelsprite'):
        await message.channel.send('https://img.pokemondb.net/artwork/large/registeel.jpg')

    if message.content.startswith('r!gimmeameem'):
        await message.channel.send(
            'Uh ok. https://www.youtube.com/watch?v=QH2-TGUlwu4')

    if message.content.startswith('r!creator'):
        await message.channel.send('lucaz_#5314')

    if message.content.startswith('r!amongus'):
        await message.channel.send('YOU ARE AN IMPOSTOR!!')

    if message.content.startswith('r!sourcecode'):
        await message.channel.send(
            'https://github.com/theultimatepokemontrainer/registeeldiscordbot'
        )

    if message.content.startswith('r!website'):
        await message.channel.send(
            'https://sites.google.com/view/registeeldiscordbot')

    if message.content.startswith('Hi Registeel'):
        await message.channel.send('Hello!')

    if message.content.startswith('GO POKEBALL!'):
        await message.channel.send('Nope!')

    if message.content.startswith('r!rumors'):
        await message.channel.send('Some say that the third Pokemon SwSh DLC is named "Cinder Citadel"')

    if message.content.startswith('r!randomnumber'):
      randomnumber = random.randint(0,1000)
      await message.channel.send(randomnumber)
      if randomnumber == 626:
        await message.channel.send('Your number is **626**. You win a cookie :)')

    if message.content.startswith('secret!e'):
     e = pb.pokemon_shape('fish')
     await message.channel.send(e.pokemon_species)

    if message.content.startswith('r!yt'):
        await message.channel.send('Subscribe here! https://www.youtube.com/channel/UCxzkAP7o94jO-5U1DcESA8w')

    if message.content.startswith('r!coinflip'):
        embedVar = discord.Embed(title="Coin Flipped!", description=random, color=0xf1c40f,)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('r!vote'):
        await message.channel.send('You can vote every 12 hours! https://top.gg/bot/809002048447184948/vote')

    
    if message.content.startswith('r!shrek'):
        await message.channel.send('https://upload.wikimedia.org/wikipedia/en/4/4d/Shrek_%28character%29.png')

    if message.content.startswith('r!poll'):
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.channel.send('👍 for yes 👎 for no')

    if message.content.startswith("r!say"):
        await message.channel.send(message.content[5:].format(message))

    if message.content.startswith('r!donkey'):
        await message.channel.send('https://i.pinimg.com/originals/b6/63/e8/b663e843f4bef374de7bd57a3d3b028c.jpg')

keep_alive()
client.run(os.getenv('TOKEN'))
