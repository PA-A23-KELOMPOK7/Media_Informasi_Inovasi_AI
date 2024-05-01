from Model.Post import PostModel as PM
import textwrap
import os
from prettytable import PrettyTable

class InfoController:
    def __init__(self):
        self.post_model = PM()

    def post_detail(self, id_post):
        os.system('cls')
        detail_post = self.post_model.data_info(id_post)
        post = detail_post
        if post:
            print(f'================================================================================')
            print(f'{post[2][:80]}')  # Judul
            print(f'ID POST : {id_post}')
            print(f'Pembuat : {post[4]}')
            print(f'Jenis : {post[0]}')
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

    def all_post(self):
        os.system('cls')
        read = self.post_model.read_accepted_info()
        if read:
            tabel_post = PrettyTable()
            tabel_post.field_names = ["Date Post", "ID Post", "Jenis Post", "Judul Post", "Creator"]
            for x in read:
                data = (x[2], x[0], x[1], x[3], x[5])
                tabel_post.add_row(data)
            print(tabel_post)
        else:
            print('Tidak Ada Postingan')
