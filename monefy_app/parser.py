import pandas as pd
from sqlalchemy.orm import sessionmaker
from db.transaction import Transaction

engine = 'postgresql://postgres:111@localhost'
Session = sessionmaker()
Session.configure(bind=engine)


def add_transaction_2_bd(monefy_data):
    sess = Session()
    df = pd.DataFrame(monefy_data)
    for i in range(len(df)):
        model = Transaction()
        model.date = df['date'][i]
        model.account = df['account'][i]
        model.category = df['category'][i]
        model.amount = df['amount'][i]
        model.currency = df['currency'][i]
        model.converted_amount = df['converted amount'][i]
        model.converted_currency = df['currency.1'][i]
        model.description = df['description'][i]
        sess.add(model)
    sess.commit()
