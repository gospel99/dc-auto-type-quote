import discord
import requests
import time
import numpy as np
import webserver
import json
from webserver import keep_alive


class MyClient(discord.Client):
    async def on_ready(self):
      print('Logged on as {0}!'.format(self.user))
      chan = self.get_channel(CHANNEL DC, buka server > buka channel > liat link di browser > /12344... paling belakang)
      #r = requests.get("https://raw.githubusercontent.com/lakuapik/quotes-indonesia/master/raw/quotes.json")
      #data = r.json()
      data = json.loads(open('data.json').read())
      while (True):
        await chan.send(np.random.choice(data, size=1)[0]['quote'])
        time.sleep(60)

keep_alive()
client = MyClient()
client.run("TOKEN DC", bot=False)
