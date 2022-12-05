import os
from utils.data import getdata
info = getdata.info()
def getcogs(ctx):
    if ctx.interaction.user.id != int(info['OwnerID']):
        return ["You don't have permission to use this command!"]
    cogs = []
    for fn in os.listdir('cogs'):
        if ctx.interaction.data['options'][1]['value'] == "":
            cogs.append(fn)
            continue
        if fn.startswith(ctx.interaction.data['options'][1]['value']):
            cogs.append(fn)
            continue
    if not cogs:
        return ["No files found with that name, or none exist"]
    return cogs