from settings import config
from data_base.dbalchemy import DBManager
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

class Keyboards:

    def __init__(self):
        """ Создание клавиатуры """

        self.markup = None
        self.DB = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        """ Установить кнопку на клавиатуре """

        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        """ Начальное меню """

        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')

        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        """ Кнопка "информация о боте" """

        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """ Кнопка "настройки" """

        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        self.markup.row(itm_btn_1)
        return self.markup

    def category_menu(self):
        """ Кнопка категорий мею """

        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('SEMIPRODUCT'))
        self.markup.add(self.set_btn('GROCERY'))
        self.markup.add(self.set_btn('ICE_CREAM'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup

    def set_inline_btn(self, name):
        """ Уставиновить внутренюю кнопку при выборе категории """

        return InlineKeyboardButton(str(name), callback_data=str(name.id))

    def set_select_category(self, category):
        """ Кнопка выбора категории """

        self.markup = InlineKeyboardMarkup(row_width=1)
        for itm in self.DB.select_all_product_category(category):
            self.markup.add(self.set_inline_btn(itm))

        return self.markup

    def remove_menu(self):
        """ Удалить клавиатуру """

        return ReplyKeyboardRemove()