from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from customer import Base

class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    phoneNumber = Column(Integer)
    passWord = Column(String)

    bnbs = relationship("Bnb", back_populates="owner")

