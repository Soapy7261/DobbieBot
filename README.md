# DobbieBot
Discord fork used: py-cord

Checkout [this to install it](https://docs.pycord.dev/en/master/installing.html).

# Self hosting
## Creating a bot
2. Create a [Discord application](https://discord.com/developers/applications/).
   You have to enable the Message Content intent.
## Configuration
Dobbiebot supports .json and .env, so you can use either one of them, however, you will need to use json for certain features, mainly the switch branch feature.

### .env
1. Create a .env file
2. Follow the env.example file and fill in the values

### .json
1. Create a config.json file
2. Follow the config.example.json file and fill in the values

## Running
1. Run `python3 -m pip install -r requirements.txt`
2. Run `python3 launcher.py` to have auto-restart, or `python3 bot.py` to not have auto-restart
3. 