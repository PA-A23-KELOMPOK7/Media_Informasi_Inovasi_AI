import mysql.connector
from Model.db_connection import koneksi

class UserModel:
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

    def read_user(self):
        try:
            query = "SELECT * FROM user"
            self.cursor.execute(query)
            user = self.cursor.fetchall()
            return user
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
            return None
        
    def detail_user(self, id_user):
        try:
            query = "SELECT nama_user, username, email_user, password FROM user WHERE id_user=%s"
            self.cursor.execute(query, (id_user,))
            detail_user = self.cursor.fetchone()
            return detail_user
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
            return None
        
    def find_user(self, username):
        try:
            query = "SELECT * FROM user WHERE username=%s"
            self.cursor.execute(query, (username,))
            user = self.cursor.fetchone()
            return user
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')

    def create_user(self, nama_user, username, email_user, password):
        try:
            query = "INSERT INTO user (nama_user, username, email_user, password) VALUES ( %s, %s, %s, %s)"
            data = (nama_user, username, email_user, password)
            self.cursor.execute(query, data)
            self.conn.commit()
            print(f'Data {username} berhasil Disimpan')
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
            self.conn.rollback()
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
            self.conn.rollback()
            return None
        
    def delete_user(self, id_user):
        try:
            query = "DELETE FROM user WHERE id_user=%s"
            self.cursor.execute(query, (id_user,))
            self.conn.commit()
            print(f'Pengguna dengan id_user {id_user} berhasil dihapus.')
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
            self.conn.rollback()
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
            return None
        
    def update_user(self, id_user, nama_user, username, email_user, password):
        try:
            query = "UPDATE user SET nama_user=%s, username=%s, email_user=%s, password=%s WHERE id_user=%s"
            data = (nama_user, username, email_user, password, id_user)
            self.cursor.execute(query, data)
            self.conn.commit()
            print(f'Data pengguna dengan ID {id_user} berhasil diperbarui.')
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
            self.conn.rollback()
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
            return None
    
    def login(self, username, password):
        pass