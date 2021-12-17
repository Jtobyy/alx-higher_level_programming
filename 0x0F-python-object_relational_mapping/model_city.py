#!/usr/bin/python3
"""
contains the class definition of a City.
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('city_id_seq'), primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship('State', backref='cities')
