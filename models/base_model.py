#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
# From sqlalchemy, base class which maintains a catalog of classes and
# tables relative to that base
Base = declarative_base()


class BaseModel:
    """
    A base class for all hbnb models
    BaseModel doesn't inherits from Base, because it cause that sqlalchemy
    try to map it to a table
    """
    # Common values to inherit from other classes
    id = Column(String(60), primary_key=True)
    # default value is the current datetime, can't be  null
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Class constructor that inits class attributes"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at':
                    kwargs['updated_at'] = (datetime.
                                            strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f'))
                if key == 'created_at':
                    kwargs['created_at'] = (datetime.
                                            strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f'))
        kwargs.pop('__class__', None)
        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary = {}
        for key, value in self.__dict__.items():
            dictionary[key] = value
        dictionary.pop("_sa_instance_state", None)
        return '[{}] ({}) {}'.format(cls, self.id, dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """ Delete the current instance from the storage """
        models.storage.delete(self)
