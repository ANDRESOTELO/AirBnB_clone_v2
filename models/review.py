#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class Review(BaseModel, Base):
    """ Review classto store review information """
    
    place_id = ""
    user_id = ""
    text = ""
