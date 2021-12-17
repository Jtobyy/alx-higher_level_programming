#!/usr/bin/python3
"""

"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
@localhost:3306/{sys.argv[3]}', pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

query = session.query(State).filter(State.name.ilike('%a%'))
for state in query:
    session.delete(state)

    session.commit()

if __name__ == '__main__':
    pass
