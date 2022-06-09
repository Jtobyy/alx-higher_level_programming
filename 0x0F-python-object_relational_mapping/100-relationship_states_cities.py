#!/usr/bin/python3
""" creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ creates the State “California” with
    the City “San Francisco” from the database
    hbtn_0e_100_usa"""
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
    @localhost:3306/{sys.argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California',
                  cities=[City(name='San Francisco'), ])
    session.add(state)
    session.commit()
