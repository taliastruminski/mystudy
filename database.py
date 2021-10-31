from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, User, Post

engine = create_engine('sqlite:///databases.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def query_all():
   posts_list = session.query(Post).all()
   return posts_list




def add_user(username, password, name):
	User_object = User(username = username, password = password, name = name)
	session.add(User_object)
	session.commit()

def add_post(text, topic):
	Post_object = Post(text = text, topic = topic)
	session.add(Post_object)
	session.commit()

def get_user_by_username(username):
  user = session.query(User).filter_by(username=username).first()
  return user