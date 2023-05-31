from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    passport = relationship("Passport", uselist=False, back_populates="person")

class Passport(Base):
    __tablename__ = 'passport'
    id = Column(Integer, primary_key=True)
    number = Column(String)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="passport")

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///Person.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# person = Person(name='Tammy Briggs')
# passport = Passport(number='A19CD4')
# person.passport = passport

# session.add(person)
# session.commit()