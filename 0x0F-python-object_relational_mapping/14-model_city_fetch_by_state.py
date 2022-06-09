#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """ prints all City objects from
    the database hbtn_0e_14_usa """
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
    @localhost:3306/{sys.argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).filter(State.id == City.state_id)\
                                      .order_by(City.id).all()

    for row in query:
        print(f'{row.State.name}: ({row.City.id}) {row.City.name}')
