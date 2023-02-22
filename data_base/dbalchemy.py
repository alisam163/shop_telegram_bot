from os import path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import config
from models.product import Products

class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance

class DBManager(metaclass=Singleton):

    def __init__(self):
        """ Создание и открытие сессии БД """
        self.engine = create_engine(config.DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()


    def select_all_product_category(self, category):
        """ Выбор всех товаров из выбранной категории """

        result = self._session.query(Products).filter_by(category_id=category).all()

        self.close()
        return result

    def close(self):
        """ Закрытие соединения """

        self._session.close()