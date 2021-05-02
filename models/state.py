#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
from models.engine.file_storage import FileStorage
import models


class State(BaseModel, Base):
    """ State class
    Attributes:
    name = input name
    cities = relationship between state table and city table"""

    __tablename__ = "states"

    # HBNB_TYPE_STORAGE = The type of storage used.
    # It can be file (using FileStorage) or db (using DBStorage)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        # Delete cascade indicates that when a parent object is marked
        # for deletion, it's related child objects should be marked too
        # https://docs.sqlalchemy.org/en/13/orm/cascades.html#cascade-delete
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        # property decorator to define getter
        @property
        def cities(self):
            """ Getter that return a list of City instances """
            # <all> method in file_storage.py returns the dictionary .__objects
            # the __objects contains all created instances
            obj_dictionary = models.storage.all(City)
            city_instances = []
            for key, value in obj_dictionary.items():
                if value.state_id == self.id:
                    city_instances.append(value)
            return (city_instances)
