# Bouncer
**Problem:**
While I was running one of my projects we had a community Discord server that was constantly under attack by bot accounts who would join the server and automatically message an advertisement to every person on our member list.

**Solution:**
Bouncer is a simply written Discord bot which will notify new users to type **!verify** in a specified channel and it will automatically assign them a "Verification" role.

**NOTE:** The Discord server must be configured to not display all members by default, Bouncer.py does **not** do this for you.

### Configuring Bouncer
Clone this repository to your desired install folder  
`git clone https://github.com/j-rockwell/bouncer.py.git`  
  
Install [Discord.py](https://discordpy.readthedocs.io/en/latest/intro.html#installing)  
**Linux/UNIX:**  
`python3 -m pip install -U discord.py`

**Windows:**  
`py -3 -m pip install -U discord.py`  

Run the bot with the proper configuration  
**--token** - Your Discord Bot Token **(REQUIRED)**  
**--prefix** - Command prefix to use for the commands, for example setting this to **~** would make the verify command **~verify**  
**--verified** - Name of your Verified role for the server this is being installed on  
**--welcome** - Name of your Welcome channel where users will be notified they must type **!verify**
