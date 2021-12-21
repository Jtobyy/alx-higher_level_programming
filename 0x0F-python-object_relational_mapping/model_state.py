#!/usr/bin/python3
"""
contains the class definition of a State and an instance
Base = declarative_base()
"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb

"""
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine(f'mysql+mysqldb://{username}:{password}\
@localhost:3306/{database}', pool_pre_ping=True)
"""

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, Sequence('state_id_seq'), primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    pass
