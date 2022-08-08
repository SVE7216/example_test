import sqlite3


class Database(object):
    """
    Simple CM for sqlite3 databases. Commits everything at exit.
    """
    def __init__(self):
        self.name = "DataBaseee.sqlite"

    def __enter__(self):
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()