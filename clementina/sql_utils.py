import sqlite3


def make_queries(path):
    """
    This function makes a simple query to the database and returns a list of tuples with data
    :param path: the path of a sqlite3 database
    :return:
    """
    try:
        db_conn = sqlite3.connect(path)
        cursor = db_conn.cursor()
        cursor.execute(
            "select title, artist, album, playcount, skipcount, rating, score  from songs where playcount > 0")
        return cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(e)
    except sqlite3.IntegrityError as e:
        print("[X] Error: {}".format(e))