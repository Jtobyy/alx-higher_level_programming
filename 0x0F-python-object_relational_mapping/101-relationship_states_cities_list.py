#!/usr/bin/python3
""" List relationship """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ lists all State objects, and
    corresponding City objects, contained in
    the database hbtn_0e_101_usa """

    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
    @localhost:3306/{sys.argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        print(f'{city.id}: {city.name}')
