import aiohttp
from utils.data.getdata import info
info = info()
async def GetBranches(ctx):
    if ctx.interaction.user.id != int(info['OwnerID']):
        return ["You don't have permission to use this command!"]
    branches = []
    async with aiohttp.ClientSession() as session:
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
