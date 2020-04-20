import parse
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime


Base = declarative_base()
DB_PATH = 'sqlite:///drivers.sqlite3'

class Driver(Base):
    __tablename__ = 'report'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Text)
    amount = sa.Column(sa.DECIMAL)
    comission = sa.Column(sa.DECIMAL)
    margin = sa.Column(sa.DECIMAL)
    cash = sa.Column(sa.DECIMAL)
    date_from = sa.Column(sa.DateTime)
    date_to = sa.Column(sa.DateTime)

class Webdata(Base):
    __tablename__ = 'webdata'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Text)
    date = sa.Column(sa.Text)
    gas = sa.Column(sa.DECIMAL)
    wash = sa.Column(sa.DECIMAL)
    cash_given = sa.Column(sa.DECIMAL)
    other_spends = sa.Column(sa.DECIMAL)
    shifts = sa.Column(sa.Integer)

def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    sessions = sessionmaker(engine)
    return sessions()


def correct_time(tfrom, tto):
    cfrom = tfrom.split("T")[0]
    ctto = tto.split("T")[0]
    return datetime.datetime.strptime(cfrom, '%Y-%m-%d'), datetime.datetime.strptime(ctto, '%Y-%m-%d')


t_from, t_to = correct_time(parse.date_from, parse.date_to)
session = connect_db()
report = Driver(name=parse.person, amount=parse.amount, comission=round(parse.comissions, 1), margin=parse.margin,
                cash=parse.cash, date_from=t_from, date_to=t_to)
session.add(report)
session.commit()
