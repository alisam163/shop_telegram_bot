from handlers.handler_com import HandlerCommand
from handlers.handler_all_text import HandlerTextAll

class HandlerMain:

    def __init__(self, bot):
        """ Регистратор обработчиков """

        self.bot = bot
        self.handler_commands = HandlerCommand(self.bot)
        self.handler_all_text = HandlerTextAll(self.bot)


    def handle(self):
        self.handler_commands.handle()
        self.handler_all_text.handle()