import abc
from markup.markup import Keyboards
from data_base.dbalchemy import DBManager

class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        """ Конструктор обработчика входящих обновлений """

        self.bot = bot
        self.keyboards = Keyboards()
        self.DB = DBManager()


    @abc.abstractmethod
    def handle(self):
        pass