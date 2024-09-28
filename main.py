import discord
import os
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import random

intents = discord.Intents.all ()
client = discord.Client (intents=intents)
bot = commands.Bot (command_prefix='/', intents=intents)

def is_me(m):
    return m.author == bot.user

@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')

@bot.command()
async def command(ctx):
    response = 'HGP input: \n select from the following: \n asdam (damage value) \n tohit (TN) \n hitloc \n srm \n srmAIV \n lrm \n lrmAIV \n mml \n lbxac \n punch (weight) \n mechkick (weight) \n psr (TN) \n fall (ton) (height) \n charge (A weight) (D weight) (speed) (TN) \n card'
    await ctx.send(response)

@bot.command()
async def asdam(ctx, num):
    input = int(num)
    total = 1
    for x in range(0,(input - 1)):
        y = random.randint(1,6)
        if (y >= 3):
            total += 1
        
        damage = total
    await ctx.send(f'{damage} points of damage')

@bot.command()
async def punch(ctx, num):
    punchtable = ["Left Arm","Right Arm","Left Torso","Right Torso","Center Torso","Head"]
    roll = random.choice(punchtable)
    input = int(num)
    damage = (input/10)
    await ctx.send(f'Punch hits the {roll} for {damage}')

@bot.command()
async def mechkick(ctx, num):
    kicktable = ["Left Leg","Right Leg"]
    input = int(num)
    roll = random.choice(kicktable)
    damage = (input/5)
    await ctx.send(f'Kicked in the {roll} for {damage}')

@bot.command()
async def fall(ctx, num, high):
    input = int(num) 
    high = int(high)
    damage = (input/10) * high
    Ftable = ["Front/Rear","Left","Right"]
    roll = random.choice(Ftable)
    response = (f'{roll} takes {damage}')
    await ctx.send(response)

@bot.command()
async def card(ctx):
    response = 'HPG network connection failure, could not retreive data. Please contact your local Comstar adept for further actions'
    await ctx.send(response)

@bot.command()
async def srm(ctx):
    button1 = Button(label='SRM 2', style=discord.ButtonStyle.green)
    button2 = Button(label='SRM 4', style=discord.ButtonStyle.green)
    button3 = Button(label='SRM 6', style=discord.ButtonStyle.green)
    async def button_callback1(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} SRMs.')
    async def button_callback2(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} SRMs.')
    async def button_callback3(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} SRMs.')
    button2.callback = button_callback2
    button1.callback = button_callback1
    button3.callback = button_callback3
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    await ctx.send('What SRM rack are you firing?', view=view)

@bot.command()
async def srmAIV(ctx):
    button1 = Button(label='SRM 2', style=discord.ButtonStyle.green)
    button2 = Button(label='SRM 4', style=discord.ButtonStyle.green)
    button3 = Button(label='SRM 6', style=discord.ButtonStyle.green)
    async def button_callback1(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} SRMs.')
    async def button_callback2(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} SRMs.')
    async def button_callback3(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} SRMs.')
    button2.callback = button_callback2
    button1.callback = button_callback1
    button3.callback = button_callback3
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    await ctx.send('What SRM rack are you firing?', view=view)

@bot.command()
async def lrm(ctx):
    button1 = Button(label='LRM 5', style=discord.ButtonStyle.green)
    button2 = Button(label='LRM 10', style=discord.ButtonStyle.green)
    button3 = Button(label='LRM 15', style=discord.ButtonStyle.green)
    button4 = Button(label='LRM 20', style=discord.ButtonStyle.green)
    async def button_callback1(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} LRMs.')
    async def button_callback2(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 3, 3, 4, 6, 6, 6, 6, 8, 8, 10, 10]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} LRMs.')
    async def button_callback3(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 5, 5, 6, 9, 9, 9, 9, 12, 12, 15, 15]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} LRMs.')
    async def button_callback4(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 6, 6, 9, 12, 12, 12, 12, 16, 16, 20, 20]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} LRMs.')
    button2.callback = button_callback2
    button1.callback = button_callback1
    button3.callback = button_callback3
    button4.callback = button_callback4
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    await ctx.send('What LRM rack are you firing?', view=view)

@bot.command()
async def lrmAIV(ctx):
    button1 = Button(label='LRM 5 with Artemis IV', style=discord.ButtonStyle.green)
    button2 = Button(label='LRM 10 with Artemis IV', style=discord.ButtonStyle.green)
    button3 = Button(label='LRM 15 with Artemis IV', style=discord.ButtonStyle.green)
    button4 = Button(label='LRM 20 with Artemis IV', style=discord.ButtonStyle.green)
    async def button_callback1(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} LRMs.')
    async def button_callback2(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 4, 6, 6, 6, 6, 8, 8, 10, 10, 10, 10]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} LRMs.')
    async def button_callback3(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 6, 9, 9, 9, 9, 12, 12, 15, 15, 15, 15]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} LRMs.')
    async def button_callback4(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 9, 12, 12, 12, 12, 16, 16, 20, 20, 20, 20]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} LRMs.')
    button2.callback = button_callback2
    button1.callback = button_callback1
    button3.callback = button_callback3
    button4.callback = button_callback4
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    await ctx.send('What LRM rack are you firing?', view=view)

@bot.command()
async def mml(ctx):
    button1 = Button(label='MML 3', style=discord.ButtonStyle.green)
    button2 = Button(label='MML 5', style=discord.ButtonStyle.green)
    button3 = Button(label='MML 7', style=discord.ButtonStyle.green)
    button4 = Button(label='MML 9', style=discord.ButtonStyle.green)

    async def button_callback1(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} MMLs.')
    async def button_callback2(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} MMLs.')
    async def button_callback3(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 2, 2, 3, 4, 4, 4, 4, 6, 6, 7, 7]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} MMLs.')
    async def button_callback4(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 3, 3, 4, 5, 5, 5, 5, 7, 7, 9, 9]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} MMLs.')
    button2.callback = button_callback2
    button1.callback = button_callback1
    button3.callback = button_callback3
    button4.callback = button_callback4
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    await ctx.send('What MML launcher are you firing?', view=view)

@bot.command()
async def lbxac(ctx):
    button1 = Button(label='LB 2-X', style=discord.ButtonStyle.green)
    button2 = Button(label='LB 5-X', style=discord.ButtonStyle.green)
    button3 = Button(label='LB 10-X', style=discord.ButtonStyle.green)
    button4 = Button(label='LB 20-X', style=discord.ButtonStyle.green)
    async def button_callback1(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} flechettes.')
    async def button_callback2(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} flechettes.')
    async def button_callback3(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 3, 3, 4, 6, 6, 6, 6, 8, 8, 10, 10]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} flechettes.')
    async def button_callback4(interaction):
        d6 = random.randint(1,6)
        roll = d6+d6
        missile_table = [0, 0, 6, 6, 9, 12, 12, 12, 12, 16, 16, 20, 20]
        missile_hit = missile_table[roll]
        hits = missile_hit
        await interaction.response.send_message(f'Hit with {hits} flechettes.')
    button2.callback = button_callback2
    button1.callback = button_callback1
    button3.callback = button_callback3
    button4.callback = button_callback4
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    await ctx.send('What LB-X Autocannon are you firing in cluster mode?', view=view)

#leaving this command in, in case stability of the fancy one is an issue. 
@bot.command()
async def attack(ctx):
    d6 = random.randint(1,6)
    roll = d6+d6
    await ctx.send(f'You rolled a {roll}')

@bot.command()
async def charge(ctx, num, ton, fast, targ):
    speed = int(fast)
    hitter = int(num)
    splat = int(ton)
    tn = int(targ)
    d6 = random.randint(1,6)
    roll = d6+d6
    slam = (hitter/10) * speed
    revenge = (splat/10)
    response = (f'{roll}, Slam! for {slam}. Takes {revenge} in return.') if roll >= tn else (f'{roll}, Dodged!')
    await ctx.send(response)

@bot.command()
async def tohit(ctx, num):
    d6 = random.randint(1,6)
    roll = d6+d6
    target = int(num)
    response = (f"{roll}, a Hit!") if roll >= target else (f"{roll}, a Miss!")
    await ctx.send(response)


@bot.command()
async def psr(ctx, num):
    d6 = random.randint(1,6)
    roll = d6+d6
    target = int(num)
    response = (f"{roll}, All good!") if roll >= target else (f"{roll}, Beefed it!")   
    await ctx.send(response)

@bot.command()
async def hitloc(ctx):
    button1 = Button(label='Front/Rear', style=discord.ButtonStyle.grey)
    button2 = Button(label="Left",style=discord.ButtonStyle.grey)
    button3 = Button(label = "Right", style=discord.ButtonStyle.grey)
    async def button_callback1(interaction):
        hitchart = ["CT-crit","RA","RA","RA","RA","RA","RL","RL","RL","RL","RT","RT","RT","RT","RT","CT","CT","CT","CT","CT","CT","LT","LT","LT","LT","LT","LL","LL","LL","LL","LA","LA","LA","LA","LA","Head"]
        roll = random.choice(hitchart)
        await interaction.response.send_message(f'{roll} was hit')   
    async def button_callback2(interaction):
        hitchartL = ["LT-crit","LL","LL","LA","LA","LA","LA","LA","LA","LA","LL","LL","LL","LL","LL","LT","LT","LT","LT","LT","LT","CT","CT","CT","CT","CT","RT","RT","RT","RT","RA","RA","RL","Head"]
        rollL = random.choice(hitchartL)
        await interaction.response.send_message(f'{rollL} was hit')
    async def button_callback3(interaction):
        hitchartR = ["RT-crit","RL","RL","RA","RA","RA","RA","RA","RA","RA","RL","RL","RL","RL","RL","RT","RT","RT","RT","RT","RT","CT","CT","CT","CT","CT","LT","LT","LT","LT","LA","LA","LL","Head"]
        rollR = random.choice(hitchartR)
        await interaction.response.send_message(f'{rollR} was hit')
    button2.callback = button_callback2
    button1.callback = button_callback1
    button3.callback = button_callback3
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    await ctx.send('Which facing are you firing into?', view=view)

load_dotenv()
bot.run(os.getenv('TOKEN'))