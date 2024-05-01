import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def koneksi():
    config = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USERNAME'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    }

    try:
        connection = mysql.connector.connect(**config)
        # print('Berhasil Terhubung Ke MYSQL Lokal')
        return connection
    except mysql.connector.Error as error:
        print(f'Gagal Terhubung: {error}')
        return None
    
    
    # config = {
    #     'host': 'localhost',
    #     'user': 'root',
    #     'password': '',
    #     'database': 'tes_mvc'
    # }