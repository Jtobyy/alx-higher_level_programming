#!/usr/bin/python3
"""
lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """lists all State objects that contain the
    letter a from the database hbtn_0e_6_usa
    """
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
    @localhost:3306/{sys.argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State) \
    .filter(State.name.ilike('%a%')) \
    .order_by(State.id.asc()):
        print(f"{state.id}: {state.name}")
