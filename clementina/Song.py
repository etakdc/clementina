from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()


class Song(Base):
    __tablename__ = 'clementine_songs'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    album = Column(String)
    artist = Column(String)
    playcount = Column(Integer)
    skipcount = Column(Integer)
    rating = Column(Float)
    clementine_score = Column(Float)

    def __init__(self, title, artist, album, pc, sc, rating, score):
        self.title = title
        self.artist = artist
        self.album = album
        self.playcount = pc
        self.skipcount = sc
        self.rating = rating
        self.clementine_score = score

    def __repr__(self):
        return f"<SONG(name={self.title}, artist={self.artist})>"
