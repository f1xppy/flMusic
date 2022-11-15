from sqlalchemy import Boolean, Column, Integer, String, JSON
from sqlalchemy.orm import relationship
from.database import Base

class Track(Base):
    __tablename__ = "Tracks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    info = Column(JSON, default = {})
    author_id = Column(Integer)

class Author(Base):
    __tablename__ = "Authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, default='')
    info = Column(JSON, default = {})
    tracks = Column(Integer)
