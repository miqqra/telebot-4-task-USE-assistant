import telebot
from telebot import types
from random import choice

#pip3 uninstall telebot
#pip3 uninstall PyTelegramBotAPI
#pip3 install PyTelegramBotAPI==2.2.3
#pip3 install --upgrade pyTelegramBotAPI

api = 'Your API'

bot = telebot.TeleBot(api)

#database : [var1, var2, right answer]
#дополнять базу можно прямо здесь, главное при этом перезапускать бота
data = {
	1:["дефИс", 'дЕфис', 'дефИс'],
	2:["аэропОрты", "аэропортЫ", "аэропОрты"],
	3:["бАнты", "бантЫ", "бАнты"],
	4:["бухгАлтеров", "бухгалтерОв", "бухгАлтеров"],
	5:["вероисповЕдание", "вероисповедАние", "вероисповЕдание"],
	6:["граждАнство", "грАжданство", "граждАнство"],
	7:['дешевИзна', 'дешевизнА', 'дешевИзна'],
	8:['диспансЕр', 'диспАнсер', 'диспансЕр']
}

#возвращает пару 1 и слово, если ответ правильный, и 0 и верный ответ, если ответ неправильный
def answer_is_right(text):
	values = list(data.values())
	for i in values:
		if text == i[2]:
			return 1, i[2]
		if text == i[1] or text == i[0]:
			return 0, i[2]
	return None, None


@bot.message_handler(func=lambda message: True)
def start(message):
	key = types.InlineKeyboardMarkup()
	word = choice(list(data.values())) 
	but_1 = types.InlineKeyboardButton(text=word[0], callback_data=word[0])
	but_2 = types.InlineKeyboardButton(text=word[1], callback_data=word[1])
	but_3 = types.InlineKeyboardButton(text="Закончить тренировку", callback_data="Закончить тренировку")
	key.add(but_1, but_2, but_3)
	bot.send_message(message.chat.id, "Блесни умом", reply_markup = key)


@bot.callback_query_handler(func=lambda message: True)
def callback_inline(message):
	is_right, correct_answer = answer_is_right(message.data)

	if message.data == "Начать тренировку":
		
		key = types.InlineKeyboardMarkup()
		word = choice(list(data.values()))
		but_1 = types.InlineKeyboardButton(text=word[0], callback_data=word[0])
		but_2 = types.InlineKeyboardButton(text=word[1], callback_data=word[1])
		but_3 = types.InlineKeyboardButton(text="Закончить тренировку", callback_data="Закончить тренировку")
		key.add(but_1, but_2, but_3)

		bot.send_message(message.from_user.id, "Блесни умом", reply_markup = key)

	if is_right == 1:
		bot.send_message(chat_id=message.message.chat.id, text="А ты неплох, продолжай в таком же духе")
		
		key = types.InlineKeyboardMarkup()
		word = choice(list(data.values())) 
		but_1 = types.InlineKeyboardButton(text=word[0], callback_data=word[0])
		but_2 = types.InlineKeyboardButton(text=word[1], callback_data=word[1])
		but_3 = types.InlineKeyboardButton(text="Закончить тренировку", callback_data="Закончить тренировку")
		key.add(but_1, but_2, but_3)

		bot.send_message(message.from_user.id, "Давай, бей рекорды", reply_markup = key)
	elif is_right == 0:
		bot.send_message(chat_id=message.message.chat.id, text=f"Ну сколько раз повторять, правильно - {correct_answer}. Не беси меня, а то реально отключусь и готовиться не сможешь")
		
		key = types.InlineKeyboardMarkup()
		word = choice(list(data.values())) 
		but_1 = types.InlineKeyboardButton(text=word[0], callback_data=word[0])
		but_2 = types.InlineKeyboardButton(text=word[1], callback_data=word[1])
		but_3 = types.InlineKeyboardButton(text="Закончить тренировку", callback_data="Закончить тренировку")
		key.add(but_1, but_2, but_3)

		bot.send_message(message.from_user.id, "Ну может сейчас сможешь правильно ответить, давай, я в тебя верю", reply_markup = key)
	elif message.data == "Закончить тренировку":
		key = types.InlineKeyboardMarkup()
		but_1 = types.InlineKeyboardButton(text="Начать тренировку", callback_data="Начать тренировку")
		key.add(but_1)
		bot.send_message(chat_id=message.message.chat.id, text="Ну и ладно, иди, в армии увидимся...", reply_markup = key)


bot.polling(none_stop=True)