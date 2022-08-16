from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, Primary_key=True)
    product_name = Column('Name', String)
    product_quantity = Column('Quantity', Integer)
    product_price = Column('Price', Integer)
    date_update = Column('Updated', Date)

    def __repr__(self):
        return f'Name: {self.product_name} Quantity: {self.product_quantity} Price: {self.product_price} Update: {self.date_update}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)

