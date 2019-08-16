
import discord
import random

Token = '____________________________________________'
Prefix = "!levi"




client = discord.Client()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!levi'):
    	if message.content == ('!levi love'):
    		msg = 'I love you so much <@455810642947997707>'.format(message)
    		await client.send_message(message.channel, msg)
    	else:
    		str = random.randint(1,9)
    		if str == 1:
    			msg = 'https://imgur.com/gqmE0Kh'.format(message)
    			await client.send_message(message.channel, msg)
    		elif str == 2:
    			msg = 'https://imgur.com/PYFWSW9'.format(message)
    			await client.send_message(message.channel, msg)
    		elif str == 3:
    			msg = 'https://imgur.com/7Mvt3H4'.format(message)
    			await client.send_message(message.channel, msg)
    		elif str == 4:
    			msg = 'https://imgur.com/uK7ANDI'.format(message)
    			await client.send_message(message.channel, msg)
    		elif str == 5:
    			msg = 'https://imgur.com/MS1WJ1j'.format(message)
    			await client.send_message(message.channel, msg)
    		elif str == 6:
    			msg = 'https://imgur.com/8Krg2oo'.format(message)
    			await client.send_message(message.channel, msg)
    		elif str == 7:
    			msg = 'https://imgur.com/FUtcpVp'.format(message)
    			await client.send_message(message.channel, msg)
    		elif str == 8:
    			msg = 'https://imgur.com/ZbVQkBj'.format(message)
    			await client.send_message(message.channel, msg)

    if message.content == ('LETS FUCK'):
    	msg = 'Do you want to be on the top or bottom'.format(message)
    	await client.send_message(message.channel, msg)
    if message.content == ('TOP'):
    	msg = 'Ok, we can do it cowboy style!'.format(message)
    	await client.send_message(message.channel, msg)
    if message.content == ('BOTTOM'):
    	msg = 'NANI?'.format(message)
    	await client.send_message(message.channel, msg)
    if message.content == ('levi'):
    	msg = 'Thats my name!'.format(message)
    	await client.send_message(message.channel, msg)
    if message.content == ('Levi'):
    	msg = 'Thats my name!'.format(message)
    	await client.send_message(message.channel, msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(Token)