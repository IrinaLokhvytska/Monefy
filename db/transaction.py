""" Module represents a Transaction. """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, String, Integer, Date
)

Base = declarative_base()


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(Date, nullable=False)
    account = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    amount = Column(String(255), nullable=False)
    currency = Column(String(30), nullable=False)
    converted_amount = Column(String(255), nullable=False)
    converted_currency = Column(String(30), nullable=False)
    description = Column(String(30), nullable=True)

    # Methods
    def __repr__(self):
        """ Show transaction object info. """
        return '<Transaction: {}>'.format(self.id)
