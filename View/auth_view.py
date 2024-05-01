from Controller.LoginController import LoginController
import os

class AuthView:
    def __init__(self):
        self.login_controller = LoginController()

    def view(self):
        try:
            while True:
                print('|==============| Selamat Datang |==============|')
                print('         Silahkan Login atau Registrasi')
                print('|==============================================|')
                print('1. Login Admin')
                print('2. Login User')
                print('3. Registrasi')
                print('4. Keluar')
                print('|==============================================|')

                pilih = input('Masukkan Pilihan Anda : ')

                if pilih == '1':
                    self.login_controller.login_admin()
                elif pilih == '2':
                    self.login_controller.login_user()        
                elif pilih == '3':
                    self.login_controller.register_user()
                elif pilih == '4':
                    print('Keluar...')
                    break
                else:
                    print('Pilihan Tidak Valid, Coba Lagi...')
        except Exception as x :
            print(f'Terjadi kesalahan saat Menginput Data : {x}')
        except KeyboardInterrupt :
            print(f'Anda Menekan Tombol Yang Salah !!')
        
# self.login_controller.read_user()



