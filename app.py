from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base




engine = create_engine('sqlite:///inventory.db', echo = False)
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, Primary_key=True)
    product_name = Column('Name', String)
    product_quantity = Column('Quantity', Integer)
    product_price = Column('Price', Integer)
    date_update = Column('Updated', Date)








