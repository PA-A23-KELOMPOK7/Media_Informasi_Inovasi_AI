import mysql.connector
from Model.db_connection import koneksi

class CommentModel:
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

    def read_comment(self, id_post):
        try:
            query = "SELECT * FROM comment WHERE id_post=%s"
            self.cursor.execute(query, (id_post,))
            comment = self.cursor.fetchall()
            return comment
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
        except Exception as exc:
            print(f'Terjadi Kesalahan : {exc}')
            return None
        
    def create_comment(self, id_post, isi_komentar, date_comment):
        try:
            query = "INSERT INTO comment (id_post, isi_komentar, date_comment) VALUES ( %s, %s, %s )"
            data = (id_post, isi_komentar, date_comment)
            self.cursor.execute(query, data)
            self.conn.commit()
            print(f'Data Komentar Pada Post {id_post} Berhasil Disimpan')
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
            self.conn.rollback()
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
            self.conn.rollback()
            return None

    def delete_comment(self, id_comment):
        try:
            query = "DELETE FROM comment WHERE id_comment=%s"
            self.cursor.execute(query, (id_comment,))
            self.conn.commit()
            print(f'Komentar Dengan ID {id_comment} Berhasil Dihapus.')
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
            self.conn.rollback()
        except Exception as exc:
            print(f'Terjadi kesalahan : {exc}')
            return None
