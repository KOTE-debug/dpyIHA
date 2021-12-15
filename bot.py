import os
import json
import random

import disnake
from disnake.ext import commands


bot = commands.Bot(command_prefix=";", intents=disnake.Intents.all())

config = {
    "only_channels": [0], #channel ID
    "token": "token"
}

with open("server.json", "r") as file:
    data = json.load(file)
    if not "phrases" in data:
        data["phrases"] = []
        json.dump(data, open("server.json", "w"), indent=4, ensure_ascii=False)


@bot.event
async def on_message(message):
    if message.channel.id in config["only_channels"] and message.content and not message.author.bot:
        if random.randint(1, 4) == 1:
            if data["phrases"]:
                await message.reply(random.choice(data["phrases"]))
                os.system("clear")
                print(", ".join(data["phrases"]))
            data["phrases"].append(message.content)
            if random.randint(1, 2) == 1:
                data["phrases"] = data["phrases"][1:]
            json.dump(data, open("server.json", "w"), indent=4, ensure_ascii=False)
            
        

bot.run(config["token"])
