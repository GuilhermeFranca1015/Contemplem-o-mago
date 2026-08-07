import discord
from discord.ext import commands
import random
from conf import token
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

lista_imagens = os.listdir("images")
lista_animais = os.listdir("animalspage")

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def animals(ctx):
    imge = random.choice(lista_animais)

    with open(f'animalspage/{imge}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def meme(ctx):
    img_name = random.choice(lista_imagens)


    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def decomposition(ctx):
    await ctx.send(f'Então você quer saber quanto tempo demora para decompor os materiais do dia a dia? O plástico demora em média de 400 a 450 anos, o alumínio demora cerca de 200 a 500 anos, o papel e o papelão demoram de 3 a 6 meses o que é bem pouco e se quiser uma lista com mais itens, mas específicos digite $decomposition2')

@bot.command()
async def decomposition2(ctx):
    await ctx.send(f'Os novos itens dessa segunda lista são a borracha (usadas nas escola) demoram de dezenas a centenas de anos para se decompor, o lápis demora em média 400 a 500 anos para sumir completamente e o último iten da lista é um copo descartável que demora em média 200 a 400 anos para se decompor. Isso mostra que o descarte incorreto pode afetar a natureza por muito tempo.')

@bot.command()
async def dice(ctx):
    resultado = random.randint(1, 6) 
    await ctx.send(f" Você rolou um: {resultado}")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run(token)
