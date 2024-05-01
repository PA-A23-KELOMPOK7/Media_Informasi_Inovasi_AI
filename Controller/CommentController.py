from Model.Comment import CommentModel as CM
from Model.Post import PostModel as PM
import datetime
import textwrap
import os

class CommentController:
    def __init__(self):
        self.comment_model = CM()
        self.post_model = PM()
        self.tanggal = datetime.date.today()


    def read_comment(self, id_post):
        read = self.comment_model.read_comment(id_post)
        if read:
            for x in read:
                isi = textwrap.fill(x[2], width=70)
                print('===============================================================================')
                print(f'ID       : {x[0]}')
                print(f'Komentar : {isi}')
                print(f'Tanggal  : {x[3]}')
            print('===============================================================================')
        else:
            print('Tidak Ada Komentar')

    def hapus_comment(self):
        os.system('cls')
        print(f'==========| Hapus Komentar |===========')
        id_comment = int(input(f'Masukkan ID : '))
        try:
            self.comment_model.delete_comment(id_comment)
        except Exception as exc:
            os.system('cls')
            print(f'Terjadi kesalahan saat menghapus comment : {exc}')
        except KeyboardInterrupt :
            os.system('cls')
            print("Anda menekan tombol yang salah !!")
            
    def create_comment(self, id_post):
        os.system('cls')
        try:
            print('===== Masukkan Komentar Anda =====')
            isi_komentar = input('Masukkan Komentar Anda : ')
            date_comment = self.tanggal
            self.comment_model.create_comment(id_post, isi_komentar, date_comment)
        except Exception as exc:
            os.system('cls')
            print(f'Terjadi kesalahan saat menghapus comment : {exc}')
        except KeyboardInterrupt:
            os.system('cls')
            print("Anda menekan tombol yang salah !!")
