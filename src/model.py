import sqlite3
from .db import Database


class ConfigModel:
    """Model of user config"""
    db = Database()

    @classmethod
    def create_config_table(cls, db: Database):
        """Create empty config  table"""
        sql = """
            CREATE TABLE config(
                token VARCHAR(255) NOT NULL,
                language VARCHAR(255) DEFAULT 'ru'
            );
        """

        with cls.db as db:
            try:
                db.execute(sql)
            except sqlite3.OperationalError as error:
                print(error)

    @classmethod
    def is_config_exits(cls) -> bool:
        """Return True if config exists, or else - False"""
        with cls.db as db:
            try:
                sql = """SELECT EXISTS(SELECT * FROM config);"""
                db.execute(sql)

            except sqlite3.OperationalError:  # case when table doest not exist
                cls.create_config_table(db)
                return False
            return True if db.fetchone()[0] else False

    @classmethod
    def remove_config(cls):
        """Remove config data"""
        sql = 'DELETE FROM config;'
        with cls.db as db:
            db.execute(sql)

    @classmethod
    def configure(cls, token, language: str):
        """Configurate user data in the Database"""
        if cls.is_config_exits():
            cls.remove_config()

        sql = """
                INSERT INTO config(token, language) 
                VALUES('{token}', '{language}');
                """.format(token=token, language=language)
        with cls.db as db:
            db.execute(sql)

    @classmethod
    def get_configure_user(cls):
        """Getting the user configuration from the database"""

        with cls.db as db:
            try:
                configure_user = db.execute("""
                        SELECT *
                        FROM config
                 """)
                return configure_user.fetchall()
            except sqlite3.OperationalError as error:  # case when table doest not exist
                print(error)
