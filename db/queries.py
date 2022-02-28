import sqlite3


class DB:
    def __init__(self, db_name):
        self.conn = None
        self.db_name = db_name

    def get_connection(self):
        self.conn = sqlite3.connect(self.db_name)

    def close_connection(self):
        self.conn.close()

    def create_table(self):
        query = """
        CREATE TABLE users (
        api_key TEXT NOT NULL PRIMARY KEY,
        url TEXT NOT NULL,
        language TEXT);
        """

        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def check_if_exists(self):
        query = """
        SELECT name FROM sqlite_master WHERE type='table'
        AND tbl_name='users';
        """
        cursor = self.conn.cursor()
        list_of_tables = cursor.execute(query).fetchall()
        self.conn.commit()
        cursor.close()

        if len(list_of_tables) == 0:
            return False

        return True

    def insert_data(self, api_key, language):
        query = """
        INSERT INTO users
        (api_key, url, language)
        VALUES (?, ?, ?);
        """

        try:
            params = (api_key, 'https://dadata.ru/', language)
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            cursor.close()
        except Exception:
            return
