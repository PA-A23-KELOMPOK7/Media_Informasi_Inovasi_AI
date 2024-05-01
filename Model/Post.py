import mysql.connector
from Model.db_connection import koneksi

class PostModel:
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

    def read_post(self):
        try:
            query = "SELECT * FROM blogpost"
            self.cursor.execute(query)
            post = self.cursor.fetchall()
            return post
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
        except Exception as exc:
            print(f'Terjadi Kesalahan : {exc}')
            return None
        
    def detail_post(self, id_post):
        try:
            query = "SELECT jenis_post, date_post, judul_post, isi_post, id_user, status FROM blogpost WHERE id_post=%s"
            self.cursor.execute(query, (id_post,))
            detail_post = self.cursor.fetchone()
            return detail_post
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
            return None
        
    def create_post(self, jenis_post, date_post, judul_post, isi_post, id_user, status):
        try:
            query = "INSERT INTO blogpost (jenis_post, date_post, judul_post, isi_post, id_user, status) VALUES ( %s, %s, %s, %s, %s, %s)"
            data = (jenis_post, date_post, judul_post, isi_post, id_user, status)
            self.cursor.execute(query, data)
            self.conn.commit()
            print(f'Data {judul_post} berhasil Disimpan')
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
            self.conn.rollback()
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
            self.conn.rollback()
            return None
    
    def read_accepted(self):
        try:
            query = "SELECT * FROM blogpost WHERE status=True"
            self.cursor.execute(query)
            post_accepted = self.cursor.fetchall()
            return post_accepted
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
        except Exception as exc:
            print(f'Terjadi Kesalahan : {exc}')
            return None
    
    def read_declined(self):
        try:
            query = "SELECT * FROM blogpost WHERE status=False"
            self.cursor.execute(query)
            post_declined = self.cursor.fetchall()
            return post_declined
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
        except Exception as exc:
            print(f'Terjadi Kesalahan : {exc}')
            return None

    def read_info(self):
        try:
            query = 'SELECT * FROM blogpost WHERE jenis_post="informasi" && status=True'
            self.cursor.execute(query)
            post_declined = self.cursor.fetchall()
            return post_declined
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
        except Exception as exc:
            print(f'Terjadi Kesalahan : {exc}')
            return None
    
    def ubah_status_true(self, id_post):
        try:
            query = "UPDATE blogpost SET status=True WHERE id_post=%s"
            self.cursor.execute(query, (id_post,))
            self.conn.commit()
            print(f'Status Postingan dengan ID {id_post} Berhasil Diperbarui')
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
            self.conn.rollback()
        except Exception as exc:
            print(f'Terjadi Kesalahan : {exc}')
            return None
    
    def ubah_status_false(self, id_post):
        try:
            query = "UPDATE blogpost SET status=False WHERE id_post=%s"
            self.cursor.execute(query, (id_post,))
            self.conn.commit()
            print(f'Status Postingan dengan ID {id_post} Berhasil Diperbarui')
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
            self.conn.rollback()
        except Exception as exc:
            print(f'Terjadi Kesalahan : {exc}')
            return None

    def hapus_postingan(self, id_post):
        try:
            query = "DELETE FROM blogpost WHERE id_post=%s"
            self.cursor.execute(query, (id_post,))
            self.conn.commit()
            print(f'Postingan Dengan ID {id_post} Berhasil Dihapus.')
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
            self.conn.rollback()
        except Exception as exc:
            print(f'Terjadi kesalahan : {exc}')
            return None
        
    def user_posts(self, id_user):
        try:
            query = "SELECT * FROM blogpost WHERE id_user=%s"
            self.cursor.execute(query, (id_user,))
            user_posts = self.cursor.fetchall()
            return user_posts
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
        except Exception as exc:
            print(f'Terjadi Kesalahan : {exc}')
            return None

    def data_post(self, id_post):
        try:
            query = "SELECT jenis_post, date_post, judul_post, isi_post, id_user FROM blogpost WHERE id_post=%s"
            self.cursor.execute(query, (id_post,))
            detail_post = self.cursor.fetchone()
            if detail_post:
                # post_data = {
                #     "ID Post": id_post,
                #     "Jenis": detail_post[0],
                #     "Tanggal": detail_post[1],
                #     "Judul": detail_post[2],
                #     "Isi": detail_post[3],
                #     "User": detail_post[4],
                # }
                return detail_post
            else:
                print("Postingan tidak ditemukan.")
                return None
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
            return None
        
    def read_accepted_info(self):
        try:
            query = "SELECT * FROM blogpost WHERE status=True AND jenis_post='informasi'"
            self.cursor.execute(query)
            post_accepted = self.cursor.fetchall()
            return post_accepted
        except mysql.connector.Error as err:
            print(f'Ada Error : {err}')
        except Exception as exc:
            print(f'Terjadi Kesalahan : {exc}')
            return None
    
    def data_info(self, id_post):
        try:
            query = "SELECT jenis_post, date_post, judul_post, isi_post, id_user FROM blogpost WHERE id_post=%s AND jenis_post='informasi' "
            self.cursor.execute(query, (id_post,))
            detail_post = self.cursor.fetchone()
            if detail_post:
                return detail_post
            else:
                print("Postingan tidak ditemukan.")
                return None
        except mysql.connector.Error as err:
            print(f'Ada Error: {err}')
        except Exception as exc:
            print(f'Terjadi kesalahan: {exc}')
            return None

