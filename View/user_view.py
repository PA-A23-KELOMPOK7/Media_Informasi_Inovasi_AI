from Controller.UserController import UserController
from Controller.PostController import PostController
from Controller.InfoController import InfoController
from Controller.CommentController import CommentController
from tkinter import Tk
import os

class UserView:
    def __init__(self, login_controller):
        self.user_controller = UserController()
        self.post_controller = PostController()
        self.info_controller = InfoController()
        self.comment_controller = CommentController()
        self.login_controller = login_controller

    def view(self):
        user = self.login_controller.logged_in
        try:
            while True:
                print('==============================')
                print('Selamat Datang Di Halaman User : ', user[1])
                print('1. Profil Anda')
                print('2. Postingan')
                print('3. Informasi Webinar & Pelatihan')
                print('4. Keluar')
                print('==============================')

                pilih = input('Masukkan Pilihan Anda : ')
                if pilih == '1': # ===== Profil User =====
                    while True:
                        print(f'||=============== PROFIL ===============||')
                        print(f'    Nama      : {user[1]}')
                        print(f'    Username  : {user[2]}')
                        print(f'    e-Mail    : {user[3]}')
                        print(f'||======================================||')
                        print(f'  1. Edit Profil')
                        print(f'  2. Postingan Anda')
                        print(f'  3. Kembali')
                        pilih = input('Masukkan Pilihan Anda : ')
                        if pilih == '1':
                            self.user_controller.user_edit(user)
                        elif pilih == '2':
                            self.post_controller.user_posts(user)
                            print('================| Pilih Aksi Anda |================')
                            print('1. Tambah Postingan')
                            print('2. Cari Postingan')
                            print('3. Pilih Postingan')
                            print('4. Kembali...')
                            print('==============================')
                            pilih = input('Masukkan Pilihan Anda : ')
                            if pilih == '1':
                                self.post_controller.create_post(user)
                            elif pilih == '2':
                                pass
                            elif pilih == '3':
                                id_post = int(input('Masukkan ID Post : '))
                                self.post_controller.detail_post(id_post)
                            elif pilih == '4':
                                print('Kembali...')
                                break
                            else:
                                print('Pilihan Anda Tidak Valid, Silahkan Coba Lagi')
                        elif pilih == '3':
                            print('Kembali...')
                            break
                        else:
                            print('Pilihan Anda Tidak Valid, Silahkan Coba Lagi')
                elif pilih == '2':  # ===== Menu Postingan =====
                    while True:
                        self.post_controller.all_post()
                        print(f'==========| Menu Postingan |==========')
                        print(f'1. Pilih Postingan')
                        print(f'2. Cari Postingan')
                        print(f'3. Kembali')
                        pilih = input('Masukkan Pilihan Anda : ')
                        if pilih == '1':
                            id_post = input('Masukkan ID Post Yang Dibutuhkan : ')
                            while True:
                                self.post_controller.post_detail(id_post)
                                self.comment_controller.read_comment(id_post)
                                print('1. Tambahkan Komentar')
                                print('2. Kembali')
                                pilih = input('Masukan Pilihan Anda : ')
                                if pilih == '1':
                                    self.comment_controller.create_comment(id_post)
                                elif pilih == '2':
                                    print('Kembali...')
                                    break
                                else:
                                    print('Pilihan Anda Salah')
                        elif pilih == '2':
                            id_post = int(input('Masukkan ID Post Yang Dicari : '))
                            while True:
                                self.post_controller.search_post(id_post)
                        elif pilih == '3':
                            print('Kembali...')
                            break
                        else:
                            print('Pilihan Anda Tidak Valid, Silahkan Coba Lagi')
                elif pilih == '3':  # ===== Menu Informasi =====
                    while True:
                        self.info_controller.all_post()
                        print(f'====| Informasi Pelatihan & Webinar |=====')
                        print(f'1. Pilih Informasi')
                        print(f'2. Cari Informasi')
                        print(f'3. Kembali')
                        pilih = input('Masukkan Pilihan Anda : ')
                        if pilih == '1':
                            id_post = input('Masukkan ID Post Yang Dibutuhkan : ')
                            while True:
                                self.info_controller.post_detail(id_post)
                                self.comment_controller.read_comment(id_post)
                                print('1. Tambahkan Komentar')
                                print('2. Kembali')
                                pilih = input('Masukan Pilihan Anda : ')
                                if pilih == '1':
                                    self.comment_controller.create_comment(id_post)
                                elif pilih == '2':
                                    print('Kembali...')
                                    break
                                else:
                                    print('Pilihan Anda Salah')
                        elif pilih == '2':
                            id_post = int(input('Masukkan ID Informasi Yang Dicari : '))
                            while True:
                                self.info_controller.search_info(id_post)
                        elif pilih == '3':
                            print('Kembali...')
                            break
                        else:
                            print('Pilihan Anda Tidak Valid, Silahkan Coba Lagi')
                elif pilih == '4':
                    print('Keluar...')
                    break
                else:
                    print('Pilihan Tidak Valid, Coba Lagi...')
        except Exception as x :
            print(f'Terjadi kesalahan saat mengakses halaman ini : {x}')
        except KeyboardInterrupt as err:
            print(f'Anda Menekan Tombol Yang Salah !!!: {err}')
    def coba(self):
        self.user_controller.read_user()
