#!/usr/bin/python3
"""
contains the class definition of a City.
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ City class model that maps to a cities table """
    __tablename__ = 'cities'

    id = Column(Integer, Sequence('city_id_seq'), primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates='cities')
