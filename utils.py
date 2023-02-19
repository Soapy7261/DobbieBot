from os import listdir, getenv
from aiohttp import ClientSession
from json import load as jsonload
from json.decoder import JSONDecodeError
from sys import exit as sysexit
try:
    from dotenv import load_dotenv
except ImportError:
    print("dotenv module not found! You will not be able to use a .env file.")
class Utils:
    @staticmethod # This is a static method, which means you don't need to create an instance of the class to use it
    def info() -> dict:
        use_json = True # Change this to False if you want to use environment variables instead of a config.json file
        response = {}
        if use_json:
            try:
                with open("config.json", "r", encoding="UTF-8") as file:
                    response = jsonload(file)
            except FileNotFoundError:
                print("config.json file not found! Please create it.")
                sysexit()
            except JSONDecodeError:
                print("config.json file is invalid! Please fix it.")
                sysexit()
            except EncodingWarning:
                print("config.json file is not encoded in UTF-8! Please fix it.")
                sysexit()
        if not use_json:
            load_dotenv()
            response = {
                "Token": getenv("TOKEN"),
                "OwnerID": getenv("OWNERID")
            }
        return response
    @staticmethod
    def get_cogs(ctx) -> list:
        info = Utils.info()
        if ctx.interaction.user.id != int(info['OwnerID']):
            return ["You don't have permission to use this command!"]
        cogs = []
        for file in listdir('cogs'):
            if ctx.interaction.data['options'][1]['value'] == "":
                cogs.append(file)
                continue
            if file.startswith(ctx.interaction.data['options'][1]['value']):
                cogs.append(file)
                continue
        if cogs == []:
            return ["No cogs found(!?)"]
        return cogs
    @staticmethod
    async def get_branches(ctx) -> list:
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
