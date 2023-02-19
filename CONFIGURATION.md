# Configuration

## File locations
If set to use a JSON file, the file must be in the root directory, if set to use environment variables, the environment variables must be set in the environment the bot is running in.

## Token
Discord bot authentication token, can be generated in the [Developer Portal](https://discord.com/developers/applications/)

| type   | JSON file | environment  |
|--------|-------------|---------------------|
| string | `Token` | `TOKEN` |

## Owner ID
The owner ID of the bot, this is used for owner only commands.

| type   | JSON file | environment  |
|--------|-------------|---------------------|
| string | `OwnerID` | `OWNERID` |

## Sharded
Whether the bot is sharded or not, only enable this if your bot is in more then 1000 servers.

| type   | JSON file | environment  |
|--------|-------------|---------------------|
| boolean | `Sharded` | `SHARDED` |

## Branch
The branch of the bot, this is used for the `pull` command to pull from the correct branch

| type   | JSON file | environment  |
|--------|-------------|---------------------|
| string | `Branch` | `BRANCH` |
