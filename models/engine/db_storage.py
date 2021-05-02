#!/usr/bin/python3
""" File to DBStorage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """ New engine DBStorage class """
    # Private class attributes
    __engine = None
    __session = None

    # Public instance methods
    def __init__(self):
        """ Constructor method """
        # Retrieve the ENVIRONMENT VARIABLES
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        data_base = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        # Engine creation <dialect = mysql // driver = mysqldb>
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, password, host, data_base),
                                      pool_pre_ping=True)

        # Drop all tables if the environment variable HBNB_ENV == test
        if env == 'test':
            # Base was declared on base_model.py
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session
        this method return a dictionary like FileStorage
        key = <class-name>.<object-id> // value = object
        """
        # dictionary to save objects like FileStorage
        objets_dictionary = {}

        # list of classes  if cls = None
        classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

        if cls is not None:
            query = self.__session.query(cls).all()
            for objects in query:
                key = "{}.{}".format(objects.__class__.__name__, objects.id)
                objets_dictionary[key] = objects
        else:
            for class_item in classes:
                objects = self.__session.query(eval(class_item)).all()
                key = "{}.{}".format(class_item, objects.id)
                # setattr() sets the value of the specified attribute
                # of the specified object
                setattr(objets_dictionary, key, objects)
        return (objets_dictionary)

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database """

        Base.metadata.create_all(self.__engine)
        # The sessionmaker factory generates new Session objects when called
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # The object scoped_session represents a registry of Session objects
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """call close on the private session"""
        self.__session.close()
