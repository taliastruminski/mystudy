from sqlalchemy import Column, Integer, String, Boolean,ForeignKey, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True)
   username = Column(String)
   password = Column(String)
   name = Column(String)


class Post(Base):
   __tablename__ = 'posts'
   id = Column(Integer, primary_key=True)
   text = Column(String)
   topic = Column(String)