from Controller.UserController import UserController
from Controller.PostController import PostController
# from Controller.LoginController import LoginController
from Controller.InfoController import InfoController
from Controller.CommentController import CommentController
import os

class AdminView():
    def __init__(self):
        self.UserController = UserController()
        # self.LoginController = LoginController()
        self.PostController = PostController()
        self.InfoController = InfoController()
        self.CommentController = CommentController()

    def view(self):
        try:
            while True:
                print('=======================================')
                print('    | Selamat Datang Di Menu Admin |   ')
                print('=======================================')
                print('1. User Management')
                print('2. Post Management')
                print('3. Keluar')
                print('=======================================')

                pilih = input('Masukkan Pilihan Anda : ')

                if pilih == '1':
                    while True:
                        print('===================================')
                        print('       |   MANAJEMEN USER    |     ')
                        print('===================================')
                        print('1. Create User')
                        print('2. Read User')
                        print('3. Edit User')
                        print('4. Delete User')
                        print('5. Kembali')
                        pilih = input('Masukkan Pilihan Anda : ')

                        if pilih == '1':
                            self.UserController.create_user()
                        elif pilih == '2':
                            self.UserController.read_user()
                        elif pilih == '3':
                            self.UserController.detail_user()
                        elif pilih == '4':
                            self.UserController.delete_user()
                        elif pilih == '5':
                            print('Kembali...')
                            break
                        else:
                            print('pilihan yang anda masukkan salah!!')
                        
                elif pilih == '2':
                    while True:
                        try:
                            print('=====================================')
                            print('     |  MANAJEMEN POSTINGAN   |      ')
                            print('=====================================')
                            print('1. Read Post')
                            print('2. Postingan Disetujui')
                            print('3. Postingan Belum Disetujui')
                            print('4. Kembali')
                            pilih = input('Masukkan Pilihan Anda : ')

                            if pilih == '1':
                                self.PostController.read_post()
                            elif pilih == '2': #Postingan Disetujui
                                self.PostController.read_accepted()
                                id_post = input('Masukkan ID Postingan Yang Akan Diedit : ')
                                self.PostController.detail_post(id_post)
                            
                                if id_post:
                                    while True:
                                        try: 
                                            print('|====================================|')
                                            print(f'Pilih Aksi Untuk Postingan {id_post}')
                                            print('|====================================|')
                                            print('1. Ubah Status')
                                            print('2. Hapus Komentar')
                                            print('3. Hapus Postingan')
                                            print('4. Kembali')
                                            pilih = input('Masukkan Pilihan Anda : ')

                                            if pilih == '1':
                                                self.PostController.ubah_status_false(id_post)
                                                break
                                            elif pilih == '2':
                                                self.CommentController.read_comment(id_post)
                                                self.CommentController.hapus_comment()
                                            elif pilih == '3':
                                                self.PostController.hapus_postingan(id_post)
                                            elif pilih == '4':
                                                print('Kembali...')
                                                break
                                            else:
                                                print('Pilihan yang anda masukkan salah !! ')
                                        except Exception as x :
                                            print(f'Terjadi kesalahan saat mengakses postingan : {x}')
                                        except KeyboardInterrupt :
                                            print("Anda Menekan Tombol Yang Salah !! ")
                                        
                            elif pilih == '3': #Postingan Belum Disetujui
                                self.PostController.read_declined()
                                id_post = input('Masukkan ID Postingan Yang Akan Diedit : ')
                                self.PostController.detail_post(id_post)

                                if id_post:
                                    while True:
                                        print('=====================================')
                                        print(f'Pilih Aksi Untuk Postingan {id_post}')
                                        print('=====================================')
                                        print('1. Ubah Status')
                                        print('2. Kembali')
                                        pilih = input('Masukkan Pilihan Anda : ')

                                        if pilih == '1':
                                            self.PostController.ubah_status_true(id_post)
                                            break
                                        elif pilih == '2':
                                            print('Kembali...')
                                            break
                                        else:
                                            print('Pilihan yang anda masukkan salah !!')
                            elif pilih == '4':
                                print('Kembali...')
                                break
                            else:
                                print('Pilihan Yang Anda Masukkan Salah !!')
                        except Exception as x :
                            print(f'Terjadi kesalahan saat mengakses postingan : {x}')
                        except KeyboardInterrupt :
                            print("Anda Menekan Tombol Yang Salah !! ")
                elif pilih == '3':
                    print('Keluar...')
                    break
                else:
                    print('Pilihan Tidak Valid, Coba Lagi...')
        except Exception as x:
            print(f'Terjadi kesalahan saat mengakses postingan : {x}')
        except KeyboardInterrupt :
            print("Anda Menekan Tombol Yang Salah !! ")
