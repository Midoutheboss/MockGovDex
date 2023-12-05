import discord
from discord.ext import commands, tasks
import random

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)

characters = {
    "Charmander": "https://example.com/charmander.png",
    "Pikachu": "https://example.com/pikachu.png",
    # Add more characters as needed
}
spawned_character = None

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    character_spawn.start()

@tasks.loop(minutes=10)
async def character_spawn():
    global spawned_character
    spawned_character = random.choice(list(characters.keys()))

@client.event
async def on_message(message):
    global spawned_character

    if message.author == client.user:
        return

    if message.content.lower() == '!collect':
        if spawned_character:
            character_name = spawned_character
            character_image_url = characters[character_name]
            await message.channel.send(f"{message.author.mention} collected {character_name}!",
                                       file=discord.File(character_image_url))
            spawned_character = None
        else:
            await message.channel.send("No character to collect right now. Try again later.")

client.run('MTE4MTY0NjU3NzgyODM3MjUyMA.G58-8u.bPjFaLCgrdPmGqhQelKKVGt40vfkY0qg1ZXo0E')
