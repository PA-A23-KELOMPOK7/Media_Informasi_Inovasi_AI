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
Program ini menggunakan beberapa library python, seperti PrettyTable, pwinput, mysqlconnector, tkinter, os, dan dotenv.
>1. PrettyTable adalah library python yang berfungsi menampilkan data dalam bentuk tabel yang terorganisir.
>2. PWInput adalah library python yang berfungsi untuk menyembunyikan kata sandi saat melakukan login atau registrasi.
>3. MySQLConnector adalah library yang berfungsi untuk menghubungkan server database ke program.
>4. tkinter adalah library python yang berfungsi untuk menampilkan graphical user interface kepada pengguna, seperti GUI postingan. 
>5. Modul os berguna untuk berinteraksi pada sistem operasi pengguna dan melakukan operasi folder dan file.
>6. Modul dotenv berguna sebagai penghubung antara file program dan file .env pada program.
---

Program ini memiliki beberapa fitur bagi penggunanya, yaitu :
>1. User
>- Melihat profil    : User dapat melihat profil yang berisikan nama, username, dan e-mail.
>- Mengubah profil   : User dapat melakukan perubahan profilnya seperti nama, username, e-mail, dan password.
>- Melihat postingan : User dapat melihat postingan user lainnya atau postingan yang dibuat user tersebut.
>- Membuat postingan : User dapat membuat postingan yang akan ditampilkan untuk user tersebut dan user lainnya.
>- Mencari postingan : User dapat mencari postingan user tersebut atau postingan dari user lainnya.
>- Melihat informasi : User dapat melihat informasi yang diberikan.
>- Membalas komentar : User dapat membuat komentar dari postingan user tersebut, postingan user lainnya, dan informasi
>- Membalas komentar : User dapat membalas komentar dari postingan user tersebut, postingan user lainnya, dan informasi
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