# Aplikasi Blog Media Informasi Untuk Inovasi AI
---

## Deskripsi Program
>Program Aplikasi Blog ini memfasilitasi pengguna untuk mendapatkan informasi terkait topik AI menggunakan data dari hasil kontribusi User melalui fitur Komunitas pada Aplikasi. Fitur komunitas memfasilitasi berbagi informasi Inovasi Digital, Ruang pemberian informasi seputar AI,  Informasi mengenai Pelatihan dan Workshop terkait Teknologi Digital dan AI, serta Mempromosikan Inovasi dalam Inovasi Digital.

>Program Aplikasi Blog ini menggunakan bahasa pemrograman python dan juga pada program ini mengimplementasikan struktur data Linked List. Program ini juga menggunakan database, database yang digunakan untuk program ini adalah MySQL yang berfungsi untuk menyimpan data admin, data user, data postingan, dan data komentar.

>Program Aplikasi Blog Ini menggunakan desain arsitektur MVC (Model, View, Controller). Penggunaan MVC pada program ini dapat memudahkan programmer untuk melakukan maintenance pada program.
---

## Struktur Program
>1. Folder Controller, folder ini berisikan file-file yang berfungsi untuk mengambil data dari Folder Model dan menghubungkan Folder Model dan Folder View.
>- File Comment Controller, file ini berisikan function-function untuk manajemen data komentar pada postingan
>- File Info Controller, file ini berisikan function untuk menampilkan postingan berjenis informasi.
>- File Linked List Controller, file ini berisikan function-function untuk manajemen data dalam bentuk struktur data Linked List yang mana datanya diambil dari database MySQL.
>- File Login Controller, file ini berisikan function-function seperti login admin, login user, dan registrasi.
>- File Post Controller, file ini berisikan function-function dari postingan, seperti menyetujui postingan.
>- File User Controller, file ini berisikan function-function untuk manajemen data user. seperti membuat user baru.
>2. Folder Model, folder ini berisikan file-file yang berfungsi untuk manipulasi data pada database
>- File Admin, file ini berfungsi untuk menyiapkan data admin dari database.
>- File Comment,file ini berfungsi untuk menyiapkan dan memanipulasi data komentar pada database.
>- File db_connection, file ini berfungsi untuk menghubungkan program ke database MySQL.
>- File Post, file ini berfungsi untuk menyiapkan dan memanipulasi data postingan pada database.
>- File User, file ini berfungsi untuk menyiapkan dan memanipulasi data user pada database.
>3. Folder View, folder ini berisikan file-file yang berfungsi untuk menampilkan halaman yang akan dilihat bagi pengguna.
>- File Admin View, file ini berfungsi untuk menampilkan menu dari admin.
>- File Auth View, file ini berfungsi untuk menampilakn halaman login admin dan login user serta registrasi untuk user.
>- File User View, file ini berfungsi untuk menampilkan menu dari user. 
>4. File .env, file ini digunakan untuk menyimpan nilai variabel yang nantinya akan digunakan untuk menghubungkan ke database MySQL.
>5. File main, file ini adalah file utama untuk menjalankan program.
---

## Fitur
Program ini menggunakan beberapa library python, seperti PrettyTable, pwinput, mysqlconnector, textwrap, os, dotenv, dan math.
>1. PrettyTable adalah library python yang berfungsi menampilkan data dalam bentuk tabel yang terorganisir.
>2. PWInput adalah library python yang berfungsi untuk menyembunyikan kata sandi saat melakukan login atau registrasi.
>3. MySQLConnector adalah library yang berfungsi untuk menghubungkan server database ke program.
>4. Modul textwrap berguna untuk menampilkan postingan pada program agar terlihat rapi.
>5. Modul os berguna untuk berinteraksi pada sistem operasi pengguna dan melakukan operasi folder dan file.
>6. Modul dotenv berguna sebagai penghubung antara file program dan file .env pada program.
>7. Modul math berfungsi sebagai pembuatan algoritma search pada program.
---

Program ini memiliki beberapa fitur bagi penggunanya, yaitu :
>1. User
>- Melihat profil    : User dapat melihat profil yang berisikan nama, username, dan e-mail.
>- Mengubah profil   : User dapat melakukan perubahan profilnya seperti nama, username, e-mail, dan password.
>- Melihat postingan : User dapat melihat postingan user lainnya atau postingan yang dibuat user tersebut.
>- Membuat postingan : User dapat membuat postingan yang akan ditampilkan untuk user tersebut dan user lainnya.
>- Mencari postingan : User dapat mencari postingan user tersebut atau postingan dari user lainnya.
>- Melihat informasi : User dapat melihat informasi yang diberikan.
>2. Admin
>- Melihat profil user : Admin dapat melihat profil user yang berisikan id user, nama user, username, e-mail user, dan password user.
>- Mengubah profil user: Admin dapat melakukan perubahan pada profil user seperti mengubah nama user, username, e-mail dan password user.
>- Menghapus user : Admin dapat menghapus user dari database.
>- Menyetujui postingan : Admin dapat menyetujui postingan baru yang telah dibuat oleh user untuk ditampilkan di halaman postingan nantinya.
>- Mengubah status postingan : Admin dapat mengubah status postingan, status berfungsi untuk menyembunyikan atau menampilkan postingan.
>- Menghapus komentar : Admin dapat menghapus komentar yang telah dibuat oleh user.
>- Menghapus postingan : Admin dapat menghapus postingan yang telah dibuat.
---

## Fungsionalitas
>1. Registrasi User.
>- User dapat melakukan registrasi agar dapat masuk ke dalam program aplikasi blog dengan mengisi formulir pendaftaran.
>2. Log-in dan Keluar
>- User dapat melakukan log-in untuk dapat masuk ke dalam program aplikasi blog. User juga dapat keluar dari program dengan memilih opsi keluar.
>3. Postingan dan Informasi
>- User dapat melihat dan membuat postingan. User dapat melihat postingan yang berisikan informasi yang telah disediakan untuk program. Pada postingan dan informasi, user dapat melakukan membuat komentar dan membalas komentar.
---

# Flowchart Program
---
## Menu Utama Program
![alt text](<assets/Menu Utama .jpg>)
---

### Login User
![alt text](<assets/Login User.jpg>)
---

### Login Admin
![alt text](<assets/Login Admin.jpg>)
---

### Registrasi User
![alt text](<assets/Registrasi User.jpg>)
---


## Menu User
Berikut adalah diagram alur program pada menu user :
![alt text](<assets/Menu Utama User.jpg>)

### Halaman User
![alt text](<assets/Halaman User.jpg>)

#### Profil User
![alt text](<assets/Halaman Profil User.jpg>)

#### Postingan User
![alt text](<assets/Postingan User.jpg>)
![alt text](<assets/Cari Postingan User.jpg>)
![alt text](<assets/Pilih Postingan User.jpg>)
---

### Semua Postingan
![alt text](<assets/Halaman Postingan-1.jpg>)

#### Cari Postingan
![alt text](<assets/Cari Postingan.jpg>)

#### Pilih Postingan
![alt text](<assets/Pilih Postingan.jpg>)
---

### Informasi Webinar dan Pelatihan
![alt text](<assets/Halaman Webinar.jpg>)
---

## Menu Admin
Berikut adalah diagram alur program pada menu admin :
![alt text](<assets/Menu Utama Admin.jpg>)
---

### Pengaturan User
![alt text](<assets/Pengaturan user.jpg>)

#### Create User
![alt text](<assets/Create user.jpg>)

#### Read User
![alt text](<assets/Read User.jpg>)

#### Update User
![alt text](<assets/Edit User.jpg>)

#### Delete User
![alt text](<assets/Delete User.jpg>)
---

### Pengaturan Postingan
![alt text](<assets/Pengaturan postingan.jpg>)

#### Postingan Belum Disetujui
![alt text](<assets/Postingan Belum Disetujui.jpg>)

#### Postingan Sudah Disetujui
![alt text](<assets/Postingan Sudah Disetujui.jpg>)
![alt text](<assets/Pengaturan Postingan Sudah Disetujui.jpg>)

# Panduan Penggunaan Program Aplikasi Blog Media Informasi Untuk Inovasi AI
---
## Halaman Utama
>Berikut adalah halaman utama dari program yang terdiri atas login admin, login user, registrasi user, dan opsi keluar program.

>![alt text](<assets/Menu Utama.png>)
---

## User
>- Registrasi User : User harus melakukan registrasi terlebih dahulu sebelum masuk ke dalam program jika user tersebut belum memiliki akun.
![alt text](<assets/0. Registrasi.png>)
>- Login User : User dapat melakukan log-in jika sudah memiliki akun untuk mengakses program.
![alt text](<assets/1. Login.png>)
![alt text](<assets/2. Menu.png>)
>- Melihat Profil : User dapat melihat profilnya secara detail. 
![alt text](<assets/3. Lihat Profil.png>)
>- Mengubah Profil : User dapat mengubah informasi profilnya. Tekan enter jika tidak ingin mengubah informasi.
![alt text](<assets/4. Edit Profil.png>)
>- Melihat Postingan : User dapat melihat postingan yang telah dibuatnya.
![alt text](<assets/5. Lihat Postingan.png>)
>- Melihat Semua Postingan : User dapat melihat semua postingan yang dibuat olehnya atau postingan dari user lain.
![alt text](<assets/7. Halaman Postingan.png>)
>- Melihat Informasi : User dapat melihat informasi pelatihan dan webinar yang telah diposting oleh user lain.
![alt text](<assets/Melihat Postingan berjenis Informasi.png>)
>- Membuat Postingan : User dapat membuat postingan untuk ditampilkan kepada user lainnya.
![alt text](<assets/6. Menambahkan Postingan.png>)
>- Membuat Komentar : User dapat membuat komentar pada postingan untuk ditampilkan kepada user lainnya, dengan cara memilih id postingan yang ingin dikomentarkan.
![alt text](<assets/8. Menambahkan komentar.png>)
>- Mencari Postingan : User dapat melakukan pencarian postingan.
---

# Panduan Penggunaan Program Aplikasi Blog Media Informasi Untuk Inovasi AI
---

---
## Admin
Berikut adalah menu utama admin : 

![alt text](<assets/2. Menu Admin.png>)
---

Berikut adalah menu pengaturan user :

![alt text](<assets/3. Menu Manajemen User.png>)
>- Create User : Admin dapat membuat akun user baru.

![alt text](<assets/4. Create User.png>)
>- Read User : Admin dapat melihat keseluruhan informasi yang dimiliki user.

![alt text](<assets/5. Read User.png>)
>- Delete User : Admin dapat menghapus akun user.

![alt text](<assets/7. Delete User.png>)
>- Update User : Admin dapat melakukan perubahan pada keseluruhan informasi yang dimiliki user.

![alt text](<assets/6. Edit User.png>)
---

Berikut adalah menu pengaturan postingan :

![alt text](<assets/8. Menu Manajemen Postingan.png>)
>- Read Postingan : Admin dapat melihat seluruh detail postingan yang ada.

![alt text](<assets/9. Read Postingan.png>)
>- Mengubah Status Postingan : Admin dapat melakukan perubahan pada status postingan untuk menyembunyikan atau menampilkan postingan.

![alt text](<assets/11.  Ubah Status.png>)
![alt text](<assets/16. Ubah Status Belum Disetujui.png>)
>- Menghapus Postingan : Admin dapat menghapus postingan yang telah diposting.

![alt text](<assets/13. Hapus Postingan.png>)
>- Menghapus Komentar : Admin dapat menghapus komentar yang ada pada postingan.

![alt text](<assets/12. Hapus Komentar.png>)
