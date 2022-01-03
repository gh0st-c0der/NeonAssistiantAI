import telebot
import random

token = open('bot_toke.txt')
token = token.read()

bot = telebot.TeleBot(token)

tags = ['неон', 'ассистент', 'неон,', 'ассистент,', 'бот', 'бот,']

@bot.message_handler(content_types=['text'])
def reply(message):
	try:
		db = open('db.txt')
		db = db.read()
		db = db.split("\n")
		db.remove(db[-1])
		
		asc = message.text.split()
		print(asc)
		
		if asc[0].lower() in tags:
			try:
				mess=message.text.split(" ")
				mess.remove(mess[0])
				if len(mess)>1:
					mess=" ".join(mess)
				else:
					mess="1"
			except:
				mess=""
				print("x")
			if message.text in db:
				bot.reply_to(message, random.choice(db))
			else:
				
				bot.reply_to(message, random.choice(db))
				if mess!="1":
					with open('db.txt', 'a') as wr:
						mes=message.text.split(" ")
						mes.remove(mes[0])
						mes= " ".join(mes)
						print(mes)
						wr.write(f"{mes}\n")
		else:
			if message.text not in db:
				with open('db.txt', 'a') as wr:
					mes=message.text
					print(mes)
					wr.write(f"{mes}\n")
	except Exception as e:
		print(e)

bot.polling(none_stop=True)