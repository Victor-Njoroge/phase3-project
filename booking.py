from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from customer import Base

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    bnb_id = Column(Integer, ForeignKey('bnbs.id'))
    check_in = Column(Date)
    check_out = Column(Date)

    customer = relationship("Customer", back_populates="bookings")
    bnb = relationship("Bnb", back_populates="bookings")

