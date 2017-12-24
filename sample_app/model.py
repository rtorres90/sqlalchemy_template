"""This file contains all the model related with the API"""
from sqlalchemy import Column, Unicode, UnicodeText, Float, Integer, ForeignKey, DateTime
from sqlalchemy import create_engine, exc as sa_exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, synonym
from sqlalchemy.orm.session import sessionmaker

URI = 'sqlite:///test.db'

engine = create_engine(URI, echo=False)
Base = declarative_base(bind=engine)


class PYBlog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)

    name = Column(Unicode(200), nullable=False)
    description = Column(Unicode(500))


def create_all():
    Base.metadata.create_all()


def transnform_seconds_to_string_time(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)
