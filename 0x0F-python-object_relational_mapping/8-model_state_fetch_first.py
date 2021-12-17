#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine(f'mysql+mysqldb://{username}:{password}\
@localhost:3306/{database}', pool_pre_ping=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
state = session.query(State).order_by(State.id.asc()).first()
if state == None:
    print("Nothing")
else:
    print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    pass
