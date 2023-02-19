from os import listdir
from aiohttp import ClientSession
class Utils:
    @staticmethod # This is a static method, which means you don't need to create an instance of the class to use it
    def info():
        use_json = True # Change this to False if you want to use environment variables instead of a config.json file
        if use_json:
            import json
            try:
                with open("config.json", "r", encoding="UTF-8") as f:
                    return json.load(f)
            except FileNotFoundError:
                print("config.json file not found! Please create it.")
                exit()
            except json.decoder.JSONDecodeError:
                print("config.json file is invalid! Please fix it.")
                exit()
        if not use_json:
            import os
            try:
                from dotenv import load_dotenv
                load_dotenv()
            except ImportError:
                print("dotenv module not found! You will not be able to use a .env file.")
            return {
                "Token": os.getenv("TOKEN"),
                "OwnerID": os.getenv("OWNERID")
            }
    @staticmethod
    def getcogs(ctx):
        info = Utils.info()
        if ctx.interaction.user.id != int(info['OwnerID']):
            return ["You don't have permission to use this command!"]
        cogs = []
        for fn in listdir('cogs'):
            if ctx.interaction.data['options'][1]['value'] == "":
                cogs.append(fn)
                continue
            if fn.startswith(ctx.interaction.data['options'][1]['value']):
                cogs.append(fn)
                continue
        if not cogs:
            return ["No files found with that name, or none exist"]
        return cogs
    @staticmethod
    async def GetBranches(ctx):
        info = Utils.info()
        if ctx.interaction.user.id != int(info['OwnerID']):
            return ["You don't have permission to use this command!"]
        branches = []
        async with ClientSession() as session:
            async with session.get('https://api.github.com/repos/Soapy7261/DobbieBot/branches') as resp:
                if resp.status == 200:
                    data = await resp.json()
                    for branch in data:
                        if ctx.interaction.data['options'][0]['value'] == "":
                            branches.append(branch['name'])
                            continue
                        if branch['name'].startswith(ctx.interaction.data['options'][0]['value']):
                            branches.append(branch['name'])
                            continue
                else:
                    branches.append("Error getting branches")
        return branches