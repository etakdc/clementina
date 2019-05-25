from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Song import Song, Base
from sql_utils import make_queries


def normalize(db_path, out_path):
    """
    This function normalizes a single database using SQLAlchemy
    :param db_path:
    :param out_path:
    :return:
    """
    data = make_queries(db_path)

    engine = create_engine(f"sqlite:///{out_path}", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for metadata in data:
        song_obj = (session.query(Song)
                    .filter(Song.title == metadata[0])
                    .filter(Song.artist == metadata[1]).first())
        if song_obj is None:
            song_obj = Song(metadata[0], metadata[1], metadata[2], metadata[3], metadata[4], metadata[5], metadata[6])
            session.add(song_obj)
        else:
            # Clementine have multiple redundant songs, so the following increments may hurt the counters accuracy
            continue
            # song_obj.playcount += metadata[3]
            # song_obj.skipcount += metadata[4]
    session.commit()
