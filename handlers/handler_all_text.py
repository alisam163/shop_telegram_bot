from settings.message import MESSAGES
from settings import config
from handlers.handler import Handler

class HandlerTextAll(Handler):

    def __init__(self, bot):
        """ Обработчик входящих текстовых обновлений в бота (клавитура) """

        super().__init__(bot)
        self.step = 0

    def pressed_btn_info(self, message):
        """ Обработчик "ИНФО" """

        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.info_menu())

    def pressed_btn_settings(self, message):
        """ Обработчик "Настройки" """
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.settings_menu())

    def pressed_btn_back(self, message):
        """ Обработчик "вернутся назад" """

        self.bot.send_message(message.chat.id, "Вы вернулись назад",
                              reply_markup=self.keyboards.start_menu())

    def pressed_btn_category(self, message):
        """ Обработчик "выбора категорий" """

        self.bot.send_message(message.chat.id, "Каталог категорий товара",
                              reply_markup=self.keyboards.remove_menu())

        self.bot.send_message(message.chat.id, "Сделайте свой выбор",
                              reply_markup=self.keyboards.category_menu())

    def pressed_btn_product(self, message, product):
        """ Обработчик категорий товаров """

        self.bot.send_message(message.chat.id, 'Категория ' + config.KEYBOARD[product],
                              reply_markup=self.keyboards.set_select_category(config.CATEGORY[product]))
        self.bot.send_message(message.chat.id, "Ok",
                              reply_markup=self.keyboards.category_menu())


    def handle(self):
        """ Дефолтные нажатия """

        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)

            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)

            # меню категорий товаров
            if message.text == config.KEYBOARD['SEMIPRODUCT']:
                self.pressed_btn_product(message, 'SEMIPRODUCT')

            if message.text == config.KEYBOARD['GROCERY']:
                self.pressed_btn_product(message, 'GROCERY')

            if message.text == config.KEYBOARD['ICE_CREAM']:
                self.pressed_btn_product(message, 'ICE_CREAM')