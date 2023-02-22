import os
from emoji import emojize

TOKEN = '6250424574:AAED9Do_CO8H6b4XXCrG7gOAmmSE5n-JMCg'

NAME_DB = 'products.db'

VERSION = '0.0.1'

AUTHOR = 'Sergo'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# кнопки клавиатуры
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}

# категории товаров
CATEGORY = {
    'SEMIPRODUCT' : 1,
    'GROCERY' : 2,
    'ICE_CREAM' : 3
}

# дефолтные команды
COMMANDS = {
    'START' : 'start',
    'HELP' : 'help',
}