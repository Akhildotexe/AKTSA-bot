import discord
from datetime import timedelta, datetime
from discord.ext import commands
from discord_together import DiscordTogether
from discord_components import DiscordComponents, Button, ButtonStyle, Interaction


client = commands.Bot(command_prefix=("t!"),help_command=None,activity=discord.Activity(type=discord.ActivityType.listening,name=" t!help | Ping Me"),intents=discord.Intents.all())
togetherControl = DiscordTogether(client)
DiscordComponents(client)

#global dlt
#dlt = "0x0037ff"

@client.event
async def on_ready():
    global up_time
    up_time= datetime.now()
    print(f'It works {client.user}')
   



@client.command()
async def help(ctx):
    e=discord.Embed(title="Help page",description = "```yaml \n \
        > 1. t!announce| To announce important info.\
        > 2. t!clear| after t!clear enter amt of msgs to clear EX: t!clear 10 \
        > 3. t!lock| after t!lock specify a channel EX: t!lock #general\
        > 4. t!unlock| after t!lock specify a channel to unlock EX: t!lock #general \n```")
    await ctx.send(embed=e)
    

@client.command()
async def announce(ctx):
    await ctx.send(embed=discord.Embed(description="waiting for your message...", color=discord.Color.green()))
    msg = await client.wait_for("message", check=lambda message:message.channel == ctx.channel and message.author == ctx.author)
    e= discord.Embed(title="Volunteering Information... ",description = f"{msg.content}",color = 0x0037ff)
    await ctx.send(embed=e)


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
@client.guild_only()
@client.has_permissions(manage_channels=True)
async def lock(ctx, *, channel:discord.TextChannel=None):
    channel = channel if channel else ctx.channel
    if channel.overwrites_for(ctx.guild.default_role) == discord.PermissionOverwrite(send_messages=False):
      text = f'{channel.mention}  is already locked.'
      color = 0xFFA500
    else:
      await channel.set_permissions(ctx.guild.default_role, send_messages=False)
      color = 0xFF0000
      text = f':lock: {channel.mention}  has been locked.'
    embed = discord.Embed(description = text, color = color)
    await ctx.send(embed=embed)


@client.command()
@client.guild_only()
@client.has_permissions(manage_channels=True)
async def unlock(ctx, channel:discord.TextChannel=None):
    channel = channel if channel else ctx.channel
    if channel.overwrites_for(ctx.guild.default_role) == discord.PermissionOverwrite(send_messages=None):
      text = f'{channel.mention}  is already unlocked.'
      color = 0xFFA500
    else:
      await channel.set_permissions(ctx.guild.default_role, send_messages=None)
      color = 0x00FF00
      text = f':unlock: {channel.mention}  has been unlocked.'
    embed = discord.Embed(description = text, color = color)
    await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument): 
        mra = discord.Embed(title=f"Error!!!", description=f" ```yaml\n\n >| {error}```", color=0xff0000) 
        await ctx.reply(embed=mra)
    elif isinstance(error, commands.MissingPermissions): 
        cmp = discord.Embed(title=f":x: Missing perms", description=f" ```yaml\n\n >| {error}```", color=0xff0000)  
        await ctx.reply(embed=cmp)
    elif isinstance(error, commands.CommandNotFound): 
        cnt = discord.Embed(title=f":x: Invalid command used ", description=f" ```yaml\n\n >| {error} \n``` ** Pls enter a valid cmd or `t!help`** ", color=0xff0000) 
    await ctx.reply(embed=cnt)



@client.event
async def on_message(message):
    if message.author.bot:return
    if "fees" in message.content:
        fe = discord.Embed(description = 'fees are already supposted to be due !!',color= 0x0037ff)
        await message.reply(embed= fe)
    elif "meeting" in message.content:
        m = discord.Embed(description = '**The next TSA meeting is Monday Nov 8th in the MEDIA CENTER.**',color = 0x0037ff)
        await message.reply(embed=m)
    elif "website" in message.content or "links" in message.content or "link" in message.content:
        we=discord.Embed(title="Helpfull Links",description = " 1. `Main Website.` https://aktsa.org/ \n \n  2. `Member login.` https://aktsa.azurewebsites.net/  \n \n \
     3.  `Remind Code 9th-10th.` https://www.remind.com/join/aktsa9-10/ (**NOTE THIS IS FOR 9th AND 10th GRADERS AND ONLY FOR 2021-2022**) \n \n 4. `Remind code 11th-12th.\
` https://www.remind.com/join/aktsa11-12/ (**NOTE THIS IS FOR 11th AND 12th GRADERS AND ONLY FOR 2021-2022**)",color=0x0037ff)
        em2 = client.get_emoji(865978943055462440)
        main_web = "https://aktsa.org/"
        member_login = "https://aktsa.azurewebsites.net/"
        remind = "https://www.remind.com/join/aktsa9-10/"
        remind_second = "https://www.remind.com/join/aktsa11-12/"

        components = [    
      [Button(label = "Main Website", custom_id = "tsa", style = 5,url=f"{main_web}",emoji=em2),
      Button(label = "Member Login", custom_id = "tsa", style = 5,url=f"{member_login}",emoji=em2),
      Button(label = "Remind For 9-10", custom_id = "tsa", style = 5,url=f"{remind}",emoji=em2)],
      [Button(label = "Remind For 11-12", custom_id = "tsa", style = 5,url=f"{remind_second}",emoji=em2)]
  ]

        await message.reply(embed=we,components=components)
    #elif "regionals" in message.content:
        #reg = discord.Embed(description = " More info about regionals will arrive later, \
        #when i get more info make sure to type `regionals` to get the latest info!",color = 0x0037ff)
        #await message.reply(embed=reg)
    elif "remind code " in message.content or "remind" in message.content:
        re= discord.Embed(description = " 1. `Remind Code 9th-10th.` https://www.remind.com/join/aktsa9-10/ (**NOTE THIS IS FOR 9th AND 10th GRADERS AND ONLY FOR 2021-2022**) \n \n 2. `Remind code 11th-12th.\
` https://www.remind.com/join/aktsa11-12/ (**NOTE THIS IS FOR 11th AND 12th GRADERS AND ONLY FOR 2021-2022**)",color=0x0037ff)
        await message.reply(embed=re)
    await client.process_commands(message)
    # elif "roosters" in messagon =e.content or "rooster" in message.content or "teams" in message.content:
    #     e= discord.Embed(description = " The roosters can be found here (**NOTE this is for 2021- 2022 season**)",color=0x0037ff)
    #     await message.reply(embed=e)
        
client.run("haha u thought ")
