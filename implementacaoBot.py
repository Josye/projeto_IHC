#Bot PoliticaBr
from telegram.ext import Updater, CommandHandler
import webbrowser

#up é uma variavel da classe Updater(atualizar), que guarda o token
up = Updater('318447429:AAGYrlheNAsw37QVj8jo-oxseV2_A7EXR2Q')

#função de inicialização do bot
def start(bot, update):
    #mensagem que será enviada
    msg = "Olá {user_name}, {cumprimento} vamos fazer as melhores?"
    #ao objeto bot, aplica-se o metodo send_message com parametros chat_id e text
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         user_name=update.message.from_user.first_name))

    

    bot.webbrowser.open("https://pt.wikipedia.org/wiki/" + search , new=2, autoraise=True)


    
    

up.dispatcher.add_handler(CommandHandler('start', start))
up.start_polling()
