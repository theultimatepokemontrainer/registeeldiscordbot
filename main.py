from keep_alive import keep_alive
import discord
import os 


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!goodbye'):
        await message.channel.send('Bye. Hope you had a great time!')

    if message.content.startswith('!invite'):
        await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=809002048447184948&permissions=19456&scope=bot')
        
    if message.content.startswith('!help'):
        await message.channel.send('https://sites.google.com/view/registeeldiscordbot/commands')

    if message.content.startswith('!rickroll'):
        await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    if message.content.startswith('!pingeveryone'):
        await message.channel.send('Hello @everyone!')
    
    if message.content.startswith('!joinserver'):
        await message.channel.send('https://discord.gg/Ev9jVf473E')

    if message.content.startswith('!whoregisteel'):
        await message.channel.send('Who I am? Well its hard to explain here but you can look at this https://bulbapedia.bulbagarden.net/wiki/Registeel')

    if message.content.startswith('!gimmeameem'):
        await message.channel.send('Uh ok. https://www.youtube.com/watch?v=QH2-TGUlwu4')

    if message.content.startswith('!creator'):
        await message.channel.send('theultimatepokemontrainer#5314')  

    if message.content.startswith('!amongus'):
        await message.channel.send('YOU ARE AN IMPOSTOR!!')

    if message.content.startswith('!sourcecode'):
        await message.channel.send('https://repl.it/@pycoding111111/Registeel-The-Discord-Bot#main.py')    


keep_alive()
client.run(os.getenv('TOKEN'))
