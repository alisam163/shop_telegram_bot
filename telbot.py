from telebot import TeleBot
from settings import config
from handlers.handler_main import HandlerMain

class Telbot:

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        """ Создание бота """

        self.token = config.TOKEN
        self.bot = TeleBot(self.token)
        self.handler = HandlerMain(self.bot)

    def start(self):
        """ Дефолтный обработчик запуска бота """

        self.handler.handle()

    def run_bot(self):
        """ Получение обновлений """

        self.start()
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = Telbot()
    bot.run_bot()
