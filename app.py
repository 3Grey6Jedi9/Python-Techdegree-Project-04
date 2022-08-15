from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base




engine = create_engine('sqlite:///inventory.db', echo = False)
Base = declarative_base()









