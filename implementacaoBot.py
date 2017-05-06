#Bot PoliticaBr
from telegram.ext import Updater, CommandHandler
import webbrowser

#up é uma variavel da classe Updater(atualizar), que guarda o token
up = Updater('Token')

#função de inicialização do bot
def start(bot, update):
    #mensagens
    msg = "Olá {user_name},{cumprimento} que bom saber que também se preocupa\
em garantir as melhores escolhas politicas para nosso país!Por favor,\
diga em que cidade você vota!"
    
    '''
    #filtrar cidade(USAR SCRAPPING)
    '''
    
    msg = "Ultimas_eleicoes"
    '''
    #mostrar os canditados eleitos (USAR SCRAPPING)
    #Indicar os projetos sugeridos e os que foram aprovados(Usar sumarização por grafo)
    '''
    
    msg = "Eleições atuais"
    '''
    #fazer atualizações de status se há ou não eleições em andamento
    #se houver: mostrar as candidaturas aprovadas
    #projetos de governo(sumarização por grafo)
    '''
    
    msg = "/Proximas_eleicoes"
    
    '''
    #manter atualizadas quando serão e quais os cargos serão eleitos
    #Atualizar as fazes do processo eleitoral
    #dar dicas de como escolher os representantes
    #dizer quais pré-candidatos aparecem nas intensões de voto(USAR SCRAPPING)
    #dizer quando serão aprovadas as candidaturas para que o eleitor possa acessar
    a opção de eleições atuais
    #mostrar biografia,  propostas politicas dos pré-candidatos com maior
    expressão de intensões de votos(USAR SCRAPPING e SUMARIZAÇÃO POR GRAFO)
    '''
    #ao objeto bot, aplica-se o metodo send_message com parametros chat_id e text
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         user_name=update.message.from_user.first_name))

    

    bot.webbrowser.open("https://pt.wikipedia.org/wiki/" + search , new=2, autoraise=True)


    
    

up.dispatcher.add_handler(CommandHandler('start', start))
up.start_polling()

