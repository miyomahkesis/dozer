import discord
from misc import out
import messages


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    out(f'still starving as {client.user}', 'b')
    STATUS = discord.Status.online
    ACTIVITY = discord.Activity(type=discord.ActivityType.watching, name="cum dry on the sidewalk")
    await client.change_presence(status=STATUS ,activity=ACTIVITY)
    # Listening to Death Magnetic

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    #try:
    await messages.message(message)    # Message !!! mhmm mhmm!!!
    #except: pass