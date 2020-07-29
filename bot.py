import discord
from discord.ext import commands
import datetime

client = commands.Bot( command_prefix = "!" )
client.remove_command( help )

@hello_words = [ "hello", "hi", "привет" ]
answer_words = [ "serverinfo", "commands" ]
goodbye_words = [ "пока", "удачи" ]


@client.event

async def on_ready():
	print( "Bot connected" )

@client.command( pass_context = True )
@commands.has_permisions( administrator = True )

async def clear( ctx, amount = 100 ):
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




token = open( f" { author.mention }  token.txt", "r" ).readline()

client.run( "NzM3NTY1OTE0MzcwOTMyNzQ2.Xx_NyQ.Ff3EeoAUoIYyNrGt3sn5-zxeBso" )
