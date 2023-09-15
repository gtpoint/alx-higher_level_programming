#!/usr/bin/python3
# Defines a State model.
# Inherits from SQLAlchemy Base and links to the MySQL table states.

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class state(Base):
  """Represents a state for a MySQL database.

    __tablename__: The name of the MySQL table.
    id : The state's id.
    name : The state's name.
  """
  __tablename__ = 'states'
  id = Column(Integer, primary_key=True)
  name =  Column(String(128), nullable=False)
