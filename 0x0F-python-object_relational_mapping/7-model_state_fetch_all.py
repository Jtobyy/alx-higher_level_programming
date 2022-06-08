#!/usr/bin/python3
""" All states via SQLAlchemy """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """  lists all State objects from the database hbtn_0e_6_usa """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
    @localhost:3306/{database}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    for state in session.query(State).order_by(State.id.asc()).all():
        print(f"{state.id}: {state.name}")
