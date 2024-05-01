from Model.User import UserModel
from Model.Admin import AdminModel
from View import admin_view
from View.user_view import UserView
import os

class LoginController:
    def __init__(self):
        self.user_model = UserModel()
        self.admin_model = AdminModel()
        self.admin_view = admin_view
        # self.user_view = user_view
        self.logged_in = None

    def login_user(self):
        os.system('cls')
        print('=============| Login User |==============')
        while True:
            try:
                username = str(input('Masukkan Username : '))
                password = str(input('Masukkan Password : '))

                user = self.user_model.find_user(username)
                if user:
                    if user[4] == password:
                        self.logged_in = user
                        user_view = UserView(self)
                        user_view.view()
                    else:
                        print('Password Anda Salah')
                else:
                    print('User Tidak Ditemukan')
            except Exception as x :
                os.system('cls')
                print(f"Terjadi Kesalahan saat login : {x}")
            except KeyboardInterrupt :
                os.system('cls')
                print("Anda Menekan Tombol Yang Salah !! ")
                
    def login_admin(self):
        os.system('cls')
        print('=============| Login Admin |==============')
        while True:
            try :
                username = str(input('Masukkan Username : '))
                password = str(input('Masukkan Password : '))

                admin = self.admin_model.find_admin(username)
                if admin:
                    if admin[3] == password:
                        self.admin_view.AdminView().view()
                    else:
                        print('Password Anda Salah')
                else:
                    print('User Tidak Ditemukan')
            except Exception as x :
                os.system('cls')
                print(f"Terjadi Kesalahan saat login : {x}")
            except KeyboardInterrupt :
                os.system('cls')
                print("Anda menekan tombol yang salah!! ")

    def register_user(self):
        os.system('cls')
        try:
            print('=========| Masukkan Data User |=========')
            nama_user = str(input('Masukkan Nama : '))
            username = str(input('Masukkan Username : '))
            email_user = str(input('Masukkan e-Mail : '))
            password = str(input('Masukkan Password : '))
            self.user_model.create_user(nama_user, username, email_user, password)
        except Exception as exc:
            print(f'Terjadi kesalahan saat membuat pengguna: {exc}')
        except KeyboardInterrupt:
            print("Anda Menekan Tombol Yang Salah!! ")
