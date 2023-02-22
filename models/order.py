from sqlalchemy import Column, String, Integer, Boolean, Float, DateTime, ForeignKey

from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base
from models.product import Products

Base = declarative_base()

class Order(Base):
    """ Заказы """

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('product.id'))
    user_id = Column(Integer)
    products = relationship(
        Products,
        backref=backref('orders',
                        userlist=True,
                        cascade='delete, all')
    )

    def __str__(self):
        return f"{self.quantity} {self.data}"