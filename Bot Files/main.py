from keep_alive import keep_alive
import discord
import os
import random
import requests
import json
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

pokemon_words = [
    "I want to be a pokemon master!", "Let's Go!", "Pikachu use Thunderbolt!",
    "YEAH!", "Pokemon!"
]

pokemon_responses = [
    "Cool!", "I like your spirit!", "You are a great person / bot!",
    "Do you know Mega Evolution?"
]

word_s = ["Hi Registeel"]

response_s = ["Hey! What's Up!"]

poke_ball = ["GO POKEBALL!"]

igot_caught = ["You have caught the wild Registeel"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Friday Night Funkin'"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('r!randomquote'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in message.content for word in pokemon_words):
        await message.channel.send(random.choice(pokemon_responses))

    if message.content.startswith('r!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('r!goodbye'):
        await message.channel.send('Bye. Hope you had a great time!')

    if message.content.startswith('r!invite'):
        await message.channel.send(
            'https://discord.com/api/oauth2/authorize?client_id=809002048447184948&permissions=19456&scope=bot'
        )

    if message.content.startswith('r!help'):
        await message.channel.send(
            'https://sites.google.com/view/registeeldiscordbot/commands')

    if message.content.startswith('r!rickroll'):
        await message.channel.send(
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    if message.content.startswith('r!pingeveryone'):
        await message.channel.send('Hello @everyone!')


    if message.content.startswith('r!whoregisteel'):
        await message.channel.send(
            'Who I am? Well its hard to explain here but you can look at this https://bulbapedia.bulbagarden.net/wiki/Registeel'
        )

    if message.content.startswith('r!gimmeameem'):
        await message.channel.send(
            'Uh ok. https://www.youtube.com/watch?v=QH2-TGUlwu4')

    if message.content.startswith('r!creator'):
        await message.channel.send('theultimatepokemontrainer#5314')

    if message.content.startswith('r!amongus'):
        await message.channel.send('YOU ARE AN IMPOSTOR!!')

    if message.content.startswith('r!sourcecode'):
        await message.channel.send(
            'https://repl.it/@pycoding111111/Registeel#main.py'
        )

    if message.content.startswith('r!website'):
        await message.channel.send(
            'https://sites.google.com/view/registeeldiscordbot')

    if any(word in message.content for word in word_s):
        await message.channel.send(random.choice(response_s))

    if any(word in message.content for word in poke_ball):
        await message.channel.send(random.choice(igot_caught))

    if message.content.startswith('r!rumors'):
        await message.channel.send('Some say that the third Pokemon SwSh DLC is named "Cinder Citadel"')

keep_alive()
client.run(os.getenv('TOKEN'))
