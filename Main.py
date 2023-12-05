import discord
from discord.ext import commands, tasks
import random
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

characters = {
    'randomcharacter': 'https://example.com/random_character_image.png',
    'wilhelmkeitel': 'https://example.com/wilhelm_keitel_image.png',
    'midou': 'https://example.com/midou_image.png'
}

inventory = {}   # Dictionary to store player inventories

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    spawn_characters.start()

@tasks.loop(seconds=30)  # Adjust the interval to 30 seconds
async def spawn_characters():
    character_name = "RandomCharacter"
    image_url = "https://example.com/random_character_image.png"
    characters[character_name.lower()] = image_url
    channel_id = YOUR_CHANNEL_ID  # Replace with the actual channel ID where you want characters to spawn
    channel = bot.get_channel(channel_id)
    await channel.send(f'A wild {character_name} appeared!\n{image_url}')

@bot.command(name='collect')
async def collect_character(ctx, character_name):
    character_name_lower = character_name.lower()
    if character_name_lower in characters:
        author_id = str(ctx.author.id)
        if author_id not in inventory:
            inventory[author_id] = []

        inventory[author_id].append(character_name_lower)
        await ctx.send(f'{character_name} collected successfully!')
    else:
        await ctx.send(f'{character_name} not found.')

@bot.command(name='inventory')
async def show_inventory(ctx):
    author_id = str(ctx.author.id)
    if author_id in inventory and inventory[author_id]:
        inventory_info = ', '.join(inventory[author_id])
        await ctx.send(f'Your inventory: {inventory_info}')
    else:
        await ctx.send('Your inventory is empty.')

bot.run('YOUR_BOT_TOKEN')  # Replace 'YOUR_BOT_TOKEN' with your actual bot token
