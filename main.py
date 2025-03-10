import discord 
from apscheduler.schedulers.asyncio import AsyncIOScheduler  
import os
 
# Replace these with your bot token and channel ID 
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
 
client = discord.Client(intents=discord.Intents.default())

 
@client.event 
async def on_ready(): 
    print(f'{client.user.name} has connected to Discord!') 
 
    # Set up the hourly task 
    scheduler = AsyncIOScheduler() 
    scheduler.add_job(send_hourly_message, 'interval', minutes=1) 
    scheduler.start() 
 
async def send_hourly_message(): 
    channel = client.get_channel(int(CHANNEL_ID)) 
    myid = '<@371915314964856834>'
    await channel.send('misa is poor lol' + myid)
 
client.run(BOT_TOKEN) 