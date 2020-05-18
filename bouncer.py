import discord
from discord.ext import commands
from discord.utils import get

import argparse

# Default Values
TOKEN = ''
COMMAND_PREFIX = '!'
CHANNEL_WELCOME = 'welcome'
ROLE_VERIFIED = 'Verified'

# Reads command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--token", help="Discord Bot Token")
parser.add_argument("--prefix", help="Command Prefix")
parser.add_argument('--verified', help="Verified Role Name")
parser.add_argument('--welcome', help='Welcome Channel Name')
args = parser.parse_args()

# Applies the Discord bot token
if (args.token):
    TOKEN = args.token

# Applies a custom command prefix
if (args.prefix):
    COMMAND_PREFIX = args.prefix

# Applies a custom verified role name
if (args.verified):
    ROLE_VERIFIED = args.verified

# Applies a custom welcome channel name
if (args.welcome):
    CHANNEL_WELCOME = args.welcome

# Throw an error message since the bot token is null
if TOKEN is None:
    print('Invalid Discord Bot Token')

# Prints configuration to the client
print('Token: ' + TOKEN)
print('Prefix: ' + COMMAND_PREFIX)
print('Verified Role: ' + ROLE_VERIFIED)
print('Welcome Channel: ' + CHANNEL_WELCOME)

bot = commands.Bot(command_prefix=COMMAND_PREFIX)

@bot.event
async def on_ready(): # Handles post-startup
    print('Logged in as: ' + bot.user.name)

@bot.event # Handles a player running the !verify command and if possible applies the role to their account
async def on_message(message):
    if message.content != COMMAND_PREFIX + "verify":
        return

    role = get(message.guild.roles, name=ROLE_VERIFIED)

    # Checks to see that the verified role exists
    if (role is None):
        await message.channel.send('Verified role not found')
        return
    
    # Get the authors role list
    existing_roles = [role.name for role in message.author.roles]

    # Checks to see that the author does not have the verified role already
    if ("Verified" in existing_roles):
        await message.channel.send('Your account is already verified')
        return

    # Apply role and send success response
    await message.author.add_roles(role)
    await message.channel.send(message.author.mention)
    await message.channel.send('Your account has been verified')
    print('Verified:', message.author.id)

# Starts the bot instance
bot.run(TOKEN)