import discord
import random
from discord.ext import commands

# token
token = <token>
# Prefix de commande pour le bot
client = commands.Bot(command_prefix='.lg ')


# Test Bot Ready
@client.event
async def on_ready():
    print("I'm alive :)")


# Chope l'utilisateur (pseudo + #xxxx) et le contenue de son msg en str et le renvoie à la console
# =========>Update : Envoie un message dans le channel un message d'avertissement à un utilisateur qui insulte par exemple =)
@client.event
async def on_message(message):
    liste_noir = ["xxx", "yyy"]  # liste d'insulte
    author = message.author
    content = message.content
    channel = message.channel
    print('{}: {}'.format(author, content))  # Renvoie à la console nom + msg
    for i in liste_noir:
        if content == i:
            await channel.send('''Attention, avertissement sur language inapproprié : 
Utilisateur: {}, 
Channel: {}
Message: "_{}_"'''.format(author, channel, content))  # Bot qui env msg sur chat
    await client.process_commands(message)


# =========>Message supprimé par utilisateur
# @client.event
# async def on_message_delete(message):
#  author = message.author
#  content = message.content
#  channel = message.channel
#  await channel.send('Message supprimé par Utilisateur: {}, sur Channel: {} : "_{}_"'.format(author, channel, content))

# =========>Commande non conventionnel : .iq ==> Qi de l'utilisateur, .echo ==> renvoie le msg rentré sans le .echo
# @client.event
# async def on_message(message):
#  channel = message.channel
#  author = message.author
#  if message.content.startswith('.iq'):
#    await channel.send("{}'s IQ = {}!".format(author, random.randint(-10, 150)))
#  if message.content.startswith('.echo'):
#    msg = message.content.split()
#    output = ''
#    for mot in msg[1:]:
#      output += mot
#      output += ' '
#    await channel.send(output)


# Commande conventionnel (Bonne manière)
# =========>Commande ping
# Note : Ajouter ctx en arg dans la commande, + appelé le bot par await ctx.send pour qu'il env le message qu'on veut!
# Note 2 : Pas besoin de specifier le préfix : Spécifié au début
# @client.command()# <== ceci et pas client.event
# async def ping(ctx):
#  await ctx.send('Pong!')
#
# =========>Commande echo
# client.command()
# async def echo(ctx, *args): #<== tjrs ajouter ctx en arg (*args = infinité arg dans une fonction)
#  out = ''
#  for mot in args:
##    out += word
#    out += ' '
#  await ctx.send(out)

# Clear
@client.command(pass_context=True)
async def clear(ctx, amount=500):
    channel = ctx.channel
    deleted = await channel.purge(limit=amount)
    await channel.send('Deleted {} message(s)'.format(len(deleted)))


@client.command()
async def dice(ctx, *args):
    channel = ctx.channel
    await channel.send('{}'.format(random.randint(0, 6)))


@client.command()
async def dice_battle(ctx, *args):
    channel = ctx.channel
    message = ctx.message
    await channel.send("Hey {}, tag someone you want to duel !".format(ctx.author))

    '''while True:
        @client.event
        async def on_message(message):
            test_author = message.author
            content = message.content

            if author == test_author:
                tag = get_tag(discord.on_message(content))
                channel.send("{} challenged {} to play dice !".format(author, tag))

    await channel.send("It's", author,"'s turn :", end=" ")
    dice_author = dice(ctx, *args)

    await channel.send(dice_author,"\nIt's", tagged_player,"'s turn", end = " ")
    dice_tagged_player = dice(ctx, *args)
    await channel.send("{}\n".format(dice_tagged_player))

    if dice_author > dice_tagged_player:
        await channel.send('{} Wins the game !'.format(author))

  elif dice_author < dice_tagged_player:
    await channel.send('{} Wins the game !'.format(tagged_player))

    else:
        await channel.send("Draw !")'''


def get_tag(message):
    content = (message).split()
    for i in range(len(content)):
        if "<@!" in content[i]:
            if len(content[i]) == 22:
                return content[i]
    return None


client.run(token)


