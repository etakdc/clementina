import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Song import Song, Base
from Directory import Directory
from sql_utils import make_queries


def normalize(db_path, normalized_database):
    """
    This function normalizes a single database using SQLAlchemy
    :param db_path: input database
    :param normalized_database: the resulting database
    :return:
    """
    try:
        data = make_queries(db_path)

        engine = create_engine(f"sqlite:///{normalized_database}", echo=False)
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
    except TypeError:
        print(f"{db_path} is not a Clementine database")

def bulk_normalize(db_path, out_path):
    """
    This function normalizes a directory of clementine databases using SQLAlchemy
    :param db_path: The root directory of databases
    :param out_path: The ouput directory to save normalized databases
    :return:
    """

    db_dir = Directory(db_path)
    db_dir.filter_files('SQLite')
    for db_file in db_dir:
        out_filename = f"{out_path}/Normalized_{os.path.basename(db_file)}"
        normalize(db_file, out_filename)


