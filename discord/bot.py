# Import Discord in cmd
import discord
import random
from discord.ext import commands

# Client to the Server
client = commands.Bot(command_prefix = '.')

# Make the bot online
@client.event
async def on_ready():
    print('Bot is ready.')
    
# Greet function
@client.command()
async def hi_bot(ctx):
    await ctx.send(' :wave: Hello, there!')

# Go to the link: weather
@client.command()
async def weather(ctx):
    await ctx.send('https://www.accuweather.com/en/hu/debrecen/188406/weather-forecast/188406')
  
# Give back different answers of messages   
@client.command(aliases=['5answer','test'])
async def _5answer(ctx, *, question):
    responses = ['You can do it!',
                 'It will be harder than you think.',
                 'Most likely.',
                 "Don't count on it",
                 'Ask again later']
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

# Connect to my Bot
client.run('Nzg2NTMwOTgyMTQzOTgzNjI2.X9HwDw.BCPsFpldqto8O1kLXn7kVbt36CQ')


