from Model.Post import PostModel as PM
from Model.Comment import CommentModel as CM
from Controller.LinkedListController import LinkedList as LL
from prettytable import PrettyTable
import os
import datetime
import pwinput
import textwrap

class PostController:
    def __init__(self):
        self.tanggal = datetime.date.today()
        self.post_model = PM()
        self.comment_model = CM()
        self.linked_list = LL()

    def tabel_read_post(self):
        tabel_post = PrettyTable()
        tabel_post.field_names = ["ID Post", "Jenis Post", "Judul Post", "Isi Post", "Creator", "Date Post", "Status"]

        return tabel_post

    def read_post(self):
        os.system('cls')
        read = self.post_model.read_post()
        if read:
            print(f'=============| Data Postingan |=============')
            post = self.tabel_read_post()
            for x in read:
                data = (x[0], x[1], x[3], x[4][:10] + '...', x[5], x[2], x[6])
                post.add_row(data)
            print(post)
        else:
            print('Tidak Ada Postingan')

    def all_post(self):
        os.system('cls')
        read = self.post_model.read_accepted()
        if read:
            tabel_post = PrettyTable()
            tabel_post.field_names = ["Date Post", "ID Post", "Jenis Post", "Judul Post", "Creator"]
            for x in read:
                data = (x[2], x[0], x[1], x[3], x[5])
                tabel_post.add_row(data)
            print(tabel_post)
        else:
            print('Tidak Ada Postingan')

    def create_post(self, user):
        
        try:
            while True:
                os.system('cls')
                print('=======| Masukkan Data Postingan |========')
                print('Jenis Post = ')
                print('1. Artikel')
                print('2. Informasi')
                print('3. Diskusi')
                pilih_jenis_post = str(input('Masukkan Jenis Post : '))
                if pilih_jenis_post == '1':
                    jenis_post = 'artikel'
                    break
                elif pilih_jenis_post == '2':
                    jenis_post = 'informasi'
                    break
                elif pilih_jenis_post == '3':
                    jenis_post = 'diskusi'
                    break
                else:
                    print('Pilihan Anda Salah')
            date_post = self.tanggal
            judul_post = str(input('Judul Postingan : '))
            isi_post = str(input('Isi Post : '))
            id_user = user[0]
            status = False
            
            self.post_model.create_post(jenis_post, date_post, judul_post, isi_post, id_user, status)
        except Exception as exc:
            print(f'Terjadi kesalahan saat membuat postingan : {exc}')
        except KeyboardInterrupt :
            os.system('cls')
            print("Anda menekan tombol yang salah!! ")

    def detail_post(self, id_post):
        os.system('cls')
        detail = self.post_model.detail_post(id_post)
        if detail:
            print(f'========| BLOGPOST {id_post} |========')
            print(f'Jenis   : {detail[0]}')
            print(f'Tanggal : {detail[1]}')
            print(f'Judul   : {detail[2]}')
            print(f'Isi     : {detail[3][:10]}...')
            print(f'USER ID : {detail[4]}')
            print(f'Status  : {detail[5]}')
            print(f'====================================')
            return id_post
        else:
            print(f'Post Dengan ID ({id_post}) Tidak Ditemukan')

    def read_accepted(self):
        os.system('cls')
        read = self.post_model.read_accepted()

        if read:
            os.system('cls')
            print(f'=============| Post Disetujui |=============')
            post = self.tabel_read_post()
            for x in read:
                data = (x[0], x[1], x[3], x[4][:10] + '...', x[5], x[2], x[6])
                post.add_row(data)
            print(post)
        else:
            print('Tidak Ada Postingan')
    

    def read_declined(self):
        os.system('cls')
        read = self.post_model.read_declined()

        if read:
            os.system('cls')
            print(f'=============| Post Belum Disetujui |=============')
            post = self.tabel_read_post()
            for x in read:
                data = (x[0], x[1], x[3], x[4][:10] + '...', x[5], x[2], x[6])
                post.add_row(data)
            print(post)
        else:
            print('Tidak Ada Postingan')


    def ubah_status_true(self, id_post):
        os.system('cls')
        print(f'Mengganti Status Post ID {id_post}')
        while True:
            try:
                pilih = str(input('Apakah Anda Yakin Ingin Mengubah Status/Setujui? (Y/T) : ')).capitalize()
                if pilih == 'Y':
                    self.post_model.ubah_status_true(id_post)
                    break
                elif pilih == 'T':
                    print('Kembali...')
                    break
                else:
                    print('Pilihan Yang Anda Masukkan Salah')
            except Exception as x:
                os.system('cls')
                print(f'Terjadi kesalahan saat mengubah status postingan  {x}')
            except KeyboardInterrupt :
                os.system('cls')
                print("Anda Menekan Tombol Yang Salah!! ")
    

    def ubah_status_false(self, id_post):
        os.system('cls')
        print(f'Mengganti Status Post ID {id_post}')
        while True:
            try:
                pilih = str(input('Apakah Anda Yakin Ingin Mengubah Status/Sembunyikan? (Y/T) : ')).capitalize()
                if pilih == 'Y':
                    self.post_model.ubah_status_false(id_post)
                    break
                elif pilih == 'T':
                    print('Kembali...')
                    break
                else:
                    print('Pilihan Yang Anda Masukkan Salah')
            except Exception as x:
                os.system('cls')
                print(f'Terjadi kesalahan saat mengubah status postingan : {x}')
            except KeyboardInterrupt :
                os.system('cls')
                print("Anda menekan tombol yang salah!! ")


    def hapus_postingan(self, id_post):
        os.system('cls')
        print(f'Menghapus Post ID {id_post}')
        while True:
            try:
                pilih = str(input('Apakah Anda Yakin Ingin Menghapus Postingan? (Y/T) : ')).capitalize()
                if pilih == 'Y':
                    self.post_model.hapus_postingan(id_post)
                    break
                elif pilih == 'T':
                    print('Kembali...')
                    break
                else:
                    print('Pilihan Yang Anda Masukkan Salah')
            except Exception as x:
                os.system('cls')
                print(f'Terjadi kesalahan saat menghapus postingan: {x}')
            except KeyboardInterrupt :
                os.system('cls')
                print("Anda menekan tombol yang salah!! ")

    def user_posts(self, user):
        os.system('cls')
        id_user = user[0]
        user_posts = self.post_model.user_posts(id_user)
        if user_posts:
            os.system('cls')
            print(f'=============| Data Postingan Anda |=============')
            post = self.tabel_read_post()
            for x in user_posts:
                data = (x[0], x[1], x[3], x[4][:10] + '...', x[5], x[2], x[6])
                post.add_row(data)
            print(post)
        else:
            print('Tidak Ada Postingan')
        
    def post_detail(self, id_post):
        os.system('cls')
        detail_post = self.post_model.data_post(id_post)
        post = detail_post
        if post:
            print(f'================================================================================')
            print(f'{post[2][:80]}')  # Judul
            print(f'ID POST : {id_post}')
            print(f'Pembuat : {post[4]}')
            print(f'Diposting : {post[2]}')
            print(f'================================================================================')

            isi_post = post[3].split("\n\n")
            for paragraph in isi_post:
                wrapped_paragraph = "\n".join(textwrap.fill(line, width=80) for line in paragraph.split("\n"))
                print(wrapped_paragraph)
                print()

            print(f'================================================================================')
        else:
            print('Data tidak ditemukan')


    def search_post(self, id_post):
        os.system('cls')
        result = self.linked_list.jumpSearch(id_post)
        if result:
            self.post_detail(result.data)
        else:
            print("Postingan tidak ditemukan")

    def search_post(self, id_post):
        os.system('cls')
        datas = self.post_model.read_accepted()
        for x in datas:
            data = x
            self.linked_list.insert(data)

        result = self.linked_list.jumpSearch(id_post)
        if result:
            self.post_detail(result.data)
        else:
            print("Postingan tidak ditemukan")
