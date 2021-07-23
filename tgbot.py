import telebot
bot_token = "1868837235:AAEGttFH1B3xwL_JH1L_Mu2XnM4NMsdt0pw"
bot = telebot.TeleBot(token=bot_token,parse_mode=None)
@bot.message_handler(commands=["Hello"])
def sendmessage(message):
    bot.reply_to(message,"Hello This Is Amit.... Welcome to Our channel")

bot.polling()
