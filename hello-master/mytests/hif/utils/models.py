from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Date, Time
from .init_db import Base

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    nickname = Column(String)

    def __init__(self, email=None, nickname='손님'):
        self.email = email
        self.nickname = nickname

    def __repr__(self):
        return 'User: %r - %r' % (self.email, self.nickname)