import telebot

bot =telebot.TeleBot('1062798887:AAHGlmS2tJDkOiag3boqZ4re8Fo2zFblhX8')


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привіт, бот")
      bot.polling()
