import discord
from random import radiant, choice
from discord.ext import commands
import datetime, pyown
import speech_recognition as sr
from discord.utils import get
import youtube_dl

import os

client = commands.Bot( command_prefix = "!" )
client.remove_command( "help" )

@hello_words = [ "hello", "hi", "привет" ]
answer_words = [ "serverinfo", "commands" ]
goodbye_words = [ "пока", "удачи" ]


@clientBot.event

async def on_ready():
	print( "Bot connected" )

	await client.change_presense( status = discord.Status.online, activity = discord.Game( "Personal Bot, Prefix - !" ) )

@client.command( pass_context = True )
@commands.has_permisions( administrator = True )

async def clear( ctx, amount : int ):
	await ctx.channel.purge( limit = amount )

@client.command( pass_context = True )

async def hello( ctx, amount = 1 ):
	await ctx.channel.purge( limit = amount )

	author = ctx.message.author
	await ctx.send( f"Hello { author.mention }" )

	@client.command( pass_context = True )

async def hello( ctx ):
	author = ctx.message.author

	await ctx.send( "Hello. Im a bot for discord" )

@client.event

async def on_message( message ):
	msg = message.content.lower()

    if msg in hello_words:
    	await message.channel.send( "Привет, я к твоим услугам" )

    if msg in answer_words:
    	await message.channel.send( "Пропиши команду !help" )
    if msg in goodbye_words:
    	await message.channel.send( "Удачи тебе!" )

@client.command( pass_context = True )
@commands.has_permisions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1 )

	await member.kick( reason = reason )
	await ctx.send( f"kick user { member.mention }" )

@client.command( pass_context = True )
@commands.has_permisions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
	emb = discord.Embed( title = "BAN!!", description = "user has be banned", colour = idscord.Colour.red() )
	await ctx.channel.purge( limit = 1 )

	await member.ban( reason = reason )

    emb.set_author( name = member.name, icon_url = member.avatar_url )
    emb.add_field( name = "Ban user", value = "Baned user : {}".format( member.mention ) )

    await ctx.send( embed = emb )

	await ctx.send( f"ban user { member.mention }" )

@client.command( pass_context = True )
@commands.has_permisions( administrator = True )

async def unban( ctx, *, member ):
	await ctx.cahnnel.purge( limit = 1 )

	banned_users = await stx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban( user )
		await ctx.send( f"Unbanned user { user.mention }" )

		return


@client.command( pass_context = True )
@commands.has_permisions( administrator = True )

async def help( ctx ):
	await ctx.cahnnel.purge( limit = 1 )
	emb = discord.Embed( title = "Административные Команды бота" )

	emb.add_field( name = "{}clear".format( PREFIX ), value = "Очистка чата" )
	emb.add_field( name = "{}kick".format( PREFIX ), value = "Выгнать участника" )
	emb.add_field( name = "{}ban".format( PREFIX ), value = "Забанить участника" )
	emb.add_field( name = "{}unban".format( PREFIX ), value = "Убрать участника со списка забаненых участников" )

	await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.has_permisions( administrator = True )

async def embed_message( ctx ):
	emb = discord.Embed( title = "Заголовок", description = "Your Text" colour = discord.Colour.purple(), url = "https://www.timeserver.ru/cities/jp/tokyo" )

	emb.set.author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = stx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_image( url = "https://media.discordapp.net/attachments/737337744589717546/737597147112800256/39c2f54e8d825cc615089333efd0d06f.gif" )
	emb.set_thumbnail( url = "https://media.discordapp.net/attachments/737337744589717546/737597146370408448/adfb243412321ebcbb0dcf98509d5783.jpg?width=437&height=677" )

	now_date = datetime.datetime.now()
	emb.add_field( name = "Time for Tokio", value = "Time :{}".format(  now_date) )

	await ctx.send( embed = emb )

@client.command()
@commands.has_permisions( administrator = True )

async def user_mute( ctx, member: discord.Member ):
	await ctx.cahnnel.purge( limit = 1 )

	mute_role = discord.utils.get( ctx.message.guild.roles, name = "JB-MUTED" )

	await member.add_roles( mute_role )
	await ctx.send( embed = emb )

	emb = discord.Embed( title = "!MUTED!", description = " { member.mention }, has be muted" colour = discord.Colour.purple(), url = "https://www.timeserver.ru/cities/jp/tokyo" )

	emb.set.author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = stx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_image( url = "https://media.discordapp.net/attachments/737337744589717546/737597147112800256/39c2f54e8d825cc615089333efd0d06f.gif" )
	emb.set_thumbnail( url = "https://images-ext-1.discordapp.net/external/kukM0K71CpZmai_qaLupXIFLoqUy_QZwVNXsaeRHsUw/https/cdn.discordapp.com/avatars/488027799987421211/7fdde727b8b22dfd9bf320a8876bd8f9.png" )

@client.event

async def on_member_join( member ):
	channel = client.get_channel( 732121529105645608 )

	role = discord.utils.get( member.guild.roles, id = 733300789484978247 )

	await member.add_roles( role )

@client.event
async def on_command_error( ctx, error ):
	pass


@clear.error
async def clear_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send( f"{ ctx.author.name }, обязательно укажите число удаляемых сообщений!" )

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f"{ ctx.author.name }, у вас нет прав администратора" )

@client.command()
async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()

@client.command()
async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnected()
	else:
		voice = await channel.connect()

@client.command()
async def play(ctx, url : str):
	song_there = os.path.isfile("song.mp3")

	try:
		if song_there:
			os.remove("song.mp3")
			print("[log] Старый файл удален ")
	except PermissionError:
		print("[log] Не удалось удалить файл ")

	await ctx.send("Пожалуйста ожидайте")

	voice = get(client.voice_clients, guild = ctx.guild)

	ydl_opts = {
        "format" : "bestaudio/best",
        "postprocessors" : [{
        	"key" : "FFmpegExtractAudio",
        	"preferredcodec" : "mp3",
        	"preferredquality" : "192"
        }],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		print("[log] Загружаю Музыку...")
		ydl.download([url])

	for file in os.listdir("./"):
		if file.endswith("mp3"):
			name = file
			print("[log] Переименовываю файл : {file}")
			os.rename(file, "song.mp3")

	voice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e : print(f"[log] {name}, музыка закончила своё проигрывание"))
	voice.source = discord.PCMVolumeTransformer(voice.source)
	voice.source.volume = 0.07

	song_name = name.rsplit("-", 2)
	await ctx.send(f"Сейчас проигрывает музыка: {song_name[0]}")

token = open( "token.txt", "r" ).readline()


client.run( token )