import typing
from sqlalchemy.orm import Session
from .database import models
from . import schemas

def create_track(db: Session, track: schemas.TrackIn) -> models.Track:
    db_track = models.Track(
        name = track.name,
        author_id = track.author_id,
    )

    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return(db_track)

def get_tracks(db: Session,skip: int = 0, limit: int = 100) -> typing.List[models.Track]:
    return db.query(models.Track) \
           .offset(skip) \
           .limit(limit) \
           .all()

def get_track(db: Session, track_id: int, track: schemas.TrackIn) -> models.Track:
    result = db.query(models.Track) \
             .filter(models.Track.id == track_id) \
             .update(track.dict())
    db.commit()

    if result == 1:
        return get_track(db, track_id)
    return None

def delete_track(db: Session, track_id:int) -> bool:
    result = db.query(models.Track) \
             .filter(models.Track.id == track_id) \
             .delete()
    db.commit()
    return result == 1

'''
----------------------------------------------------------------------------------------------------------------------------------------------------
'''


def create_author(db: Session, author: schemas.AuthorIn) -> models.Author:
    db_author = models.Author(
        name = author.name,
        description = author.description,
    )

    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return(db_author)

def get_authors(db: Session,skip: int = 0, limit: int = 100) -> typing.List[models.Author]:
    return db.query(models.Author) \
           .offset(skip) \
           .limit(limit) \
           .all()

def get_author(db: Session, author_id: int, author: schemas.AuthorIn) -> models.Author:
    result = db.query(models.Author) \
             .filter(models.Author.id == author_id) \
             .update(author.dict())
    db.commit()

    if result == 1:
        return get_track(db, author_id)
    return None

def delete_author(db: Session, author_id:int) -> bool:
    result = db.query(models.Author) \
             .filter(models.Author.id == author_id) \
             .delete()
    db.commit()
    return result == 1