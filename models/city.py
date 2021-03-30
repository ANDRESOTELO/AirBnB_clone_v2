#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    Class City that inherits from BaseModel
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"
        state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""
