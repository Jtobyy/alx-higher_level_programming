#!/usr/bin/python3
"""
Adds an object to a database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
@localhost:3306/{sys.argv[3]}', pool_pre_ping=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

state = State(name='Louisiana')
session.add(state)
session.commit()

query = session.query(State).filter(State.id==state.id).first()
print(query.id)


if __name__ == '__main__':
    pass
