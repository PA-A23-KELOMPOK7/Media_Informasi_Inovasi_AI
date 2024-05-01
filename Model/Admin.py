import mysql.connector
from Model.db_connection import koneksi


class AdminModel:
    def __init__(self):
        self.conn = koneksi()
        self.cursor = self.conn.cursor()

    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def find_admin(self, username):
        try: 
            query = "SELECT * FROM admin WHERE username=%s"
            self.cursor.execute(query, (username,))
            admin = self.cursor.fetchone()
            return admin
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
