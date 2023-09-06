from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    phoneNumber = Column(Integer)
    passWord = Column(String)

    bookings = relationship("Booking", back_populates="customer")
