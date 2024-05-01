from Model.User import UserModel as UM
import os

class UserController:
    def __init__(self):
        self.user_model = UM()

    def read_user(self):
        os.system('cls')
        read = self.user_model.read_user()
        
        if read:
            print('===============| DATA USER |===============')
            for x in read:
                print(x)
        else:
            print('Tidak ada pengguna')


    def detail_user(self):
        try :
            os.system('cls')
            print(f'==========| EDIT USER |==========')
            id_user = int(input('Masukkan ID : '))
            detail = self.user_model.detail_user(id_user)
            if detail:
                print(f'Data User Dengan ID ({id_user}) :')
                print(f'Nama     : ({detail[0]})')
                print(f'Username : ({detail[1]})')
                print(f'Email    : ({detail[2]})')
                print(f'Password : ({detail[3]})')
                while True:
                    try:
                        print('Masukkan Data Baru (Enter Jika Tidak Ingin Mengubah)')
                        nama_user = str(input(f'Masukkan Nama Baru : ') or detail[0])
                        username = str(input(f'Masukkan Username Baru : ') or detail[1])
                        email_user = str(input(f'Masukkan Email Baru : ') or detail[2])
                        password = str(input(f'Masukkan password Baru : ') or detail[3])

                        self.user_model.update_user(id_user, nama_user, username, email_user, password)
                        break
                    except Exception as x:
                        print(f'Terjadi kesalahan saat mengedit pengguna : ({x})')
                    except KeyboardInterrupt:
                        print("Anda menekan tombol yang salah !! ")
            else:
                print(f'Pengguna Dengan ID ({id_user}) Tidak Ditemukan')
        except Exception as xg:
            print(f"Terjadi kesalahan saat mengedit pengguna : {xg} ")
        except KeyboardInterrupt :
            os.system('cls')
            print("Anda Menekan Tombol Yang Salah !! ")
    

    def user_edit(self, user):
        try:
            os.system('cls')
            print('=========| Data Lama Anda |=========')
            print(f'Nama      : {user[1]}')
            print(f'Username  : {user[2]}')
            print(f'E-mail    : {user[3]}')
            print('Masukkan Data Baru Anda (Enter Jika Tidak Ingin Mengubah)')
            nama_user = str(input(f'Masukkan Nama Baru : ') or user[1])
            username = str(input(f'Masukkan Username Baru : ') or user[2])
            email_user = str(input(f'Masukkan Email Baru : ') or user[3])
            password = user[4]
            id_user = user[0]
            while True:
                simpan = input('Apakah Anda Ingin Menyimpan Data? (Y/T)').capitalize()
                if simpan == 'Y':
                    self.user_model.update_user(id_user, nama_user, username, email_user, password)
                    break
                elif simpan == 'T':
                    print('Kembali...')
                    break
                else:
                    print('Pilihan Yang Anda Masukkan Salah')
        except Exception as exc :
            print(f'Terjadi kesalahan saat mengedit pengguna: {exc}')
        except KeyboardInterrupt :
            os.system('cls')
            print("Anda Menekan Tombol Yang Salah !! ")


    def delete_user(self):
        try :
            os.system('cls')
            print(f'==========| DELETE USER |==========')
            id_user = input(f'Masukkan ID : ')
            if id_user == '0':
                print('Kembali...')
                return
            else:
                try:
                    id_user = int(id_user)
                    self.user_model.delete_user(id_user)
                except Exception as exc:
                    os.system('cls')
                    print(f'Terjadi kesalahan saat menghapus pengguna: {exc}')
                except KeyboardInterrupt :
                    os.system('cls')
                    print("Anda menekan tombol yang salah!! ")
        except Exception as exc :
            print(f'Terjadi kesalahan saat menghapus pengguna: {exc}')
        except KeyboardInterrupt :
            os.system('cls')
            print("Anda Menekan Tombol Yang Salah !! ")
            
            
    def create_user(self):
        try:
            os.system('cls')
            print('=========| Masukkan Data User |=========')
            nama_user = str(input('Masukkan Nama : '))
            username = str(input('Masukkan Username : '))
            email_user = str(input('Masukkan e-Mail : '))
            password     = str(input('Masukkan Password : '))
            self.user_model.create_user(nama_user, username, email_user, password)
        except Exception as exc:
            os.system('cls')
            print(f'Terjadi kesalahan saat membuat pengguna: {exc}')
        except KeyboardInterrupt :
            os.system('cls')
            print("Anda Menekan Tombol Yang Salah!! ")


    def edit_user(self, id_user, nama_user, username, email_user, password):
        try:
            os.system('cls')
            self.user_model.edit_user(id_user, nama_user, username, email_user, password)
        except Exception as exc:
            os.system('cls')
            print(f'Terjadi kesalahan saat mengedit pengguna: {exc}')
        except KeyboardInterrupt :
            os.system('cls')
            print("Anda Menekan Tombol Yang Salah!! ")