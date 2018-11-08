import logging
import telegram.ext as telext
import pyborg
from settings import settings
from time import sleep

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
class Main():
    def __init__(self):
        self.Pyborg = pyborg.pyborg(settings.get('gentbot'))
        self.Learning = settings.get('gentbot').get('learning')
        self.ReplyRate = settings.get('gentbot').get('replyrate')
        self.Name = settings.get('gentbot').get('name')

        self.updater = telext.Updater(token=settings.get('telegram').get('token'))

        # Setting up handlers
        dispatcher = self.updater.dispatcher
        gent_handler = telext.MessageHandler(telext.Filters.text, self.process)

        # Adding handlers
        dispatcher.add_handler(gent_handler)
        dispatcher.add_handler(telext.CommandHandler("save", self.save))

    def save(self, bot, update):
        self.Pyborg.save_all()
    
    def output(self, message, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=message)

    def process(self, bot, update):
        body = update.message.text
        print('recv: ', body)
        owner = 1
        replyrate = 100 if self.Name in body.lower() else self.ReplyRate
        self.Pyborg.process_msg(self, body, replyrate, self.Learning, owner, bot, update)
    
    def run(self):
        self.updater.start_polling()
        self.updater.idle()
    

main = Main()
main.run()
