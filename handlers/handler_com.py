from handlers.handler import Handler

class HandlerCommand(Handler):

    def __init__(self, bot):
        """ Конструктор команд """

        super().__init__(bot)

    def pressed_btn_start(self, message):
        """ Обработчик команды START """

        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' здравствуйте! Жду дальнейших задач',
                              reply_markup=self.keyboards.start_menu())

    def handle(self):
        """ Дефолтный обработчик """

        @self.bot.message_handler(commands=['start'])
        def handle(message):
            print(message)
            if message.text == '/start':
                self.pressed_btn_start(message)