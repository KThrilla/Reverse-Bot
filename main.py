
import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if '<@!870904895123914754>' in message.content or '<@870904895123914754>' in message.content and message.channel.name == 'bot-stuff':
      msg = message.content.split(">",1)[1]
      reverse_msg = msg[::-1]
      await message.channel.send(reverse_msg)
      return

keep_alive()
client.run(os.environ['BotToken'])
