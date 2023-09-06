from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from customer import Base

class Bnb(Base):
    __tablename__ = 'bnbs'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    location = Column(String)
    address = Column(String)
    price = Column(Integer)
    name = Column(String)
    status = Column(String)

    owner = relationship("Owner", back_populates="bnbs")
    bookings = relationship("Booking", back_populates="bnb")

