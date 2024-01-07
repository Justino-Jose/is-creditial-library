import mysql.connector 
from mysql.connector import Error
import pandas as pd
import datetime


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db)
        print("MySQL database connection successfull")
    except Error as err:
        print(f"Error: {err}")
    return connection


nama_host = "localhost"
user = "root"
password = "topg"
db = "db_lib"


connection = create_db_connection(nama_host, user, password, db)


def add_new_user():
   
    mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
    mycursor = mydb.cursor()
    
  
    nama_user = input("Input Nama User: ")
    tgl_user = input("Input Tanggal Lahir(YYYY-MM-DD): ")
    pek_user = input("Input Pekerjaan: ")
    alamat_user = input("Input Alamat: ")
    

    sql = f"INSERT INTO user(nama_user, tanggal_lahir, pekerjaan, alamat) VALUES ('{nama_user}', '{tgl_user}', '{pek_user}', '{alamat_user}')"         
    mycursor.execute(sql)
    mydb.commit()
    
    #Print querry berhasil dieksekusi
    print("Query berhasil dieksekusi")
    print("-------------------------")
    print("Data berhasil ditambahkan")
    
 
def add_new_book():
  
    mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
    mycursor = mydb.cursor()
    
  
    id_buku = input("Input Kode Buku: ")
    nama_buku = input("Input Nama Buku: ")
    category_buku = input("Input Kategori Buku: ")
    stock_buku = input("Input Stock Buku: ")
    
  
    sql = f"INSERT INTO buku VALUES ({id_buku}, '{nama_buku}', '{category_buku}', {stock_buku})"         
    mycursor.execute(sql)
    mydb.commit()
    
   
    print("Query berhasil dieksekusi")
    print("-------------------------")
    print("Data berhasil ditambahkan")


def add_new_trans():
    #Koneksikan dengan SQL
    mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
    mycursor = mydb.cursor()
    
    
    id_user_pinjam = input("Input ID Peminjaman: ")
    id_buku_pinjam = input("Input ID Buku: ")
    nama_user_pinjam = input("Input Nama Peminjam: ")
    nama_buku_pinjam = input("Input Nama Buku: ")
    tanggal_pinjam = datetime.datetime.today()
    tanggal_kembali = tanggal_pinjam + datetime.timedelta(days=3)
    
    
    sql = f"INSERT INTO peminjaman VALUES ('{id_user_pinjam}', '{id_buku_pinjam}', '{nama_user_pinjam}', '{nama_buku_pinjam}','{tanggal_pinjam.strftime('%Y-%m-%d')}', '{tanggal_kembali.strftime('%Y-%m-%d')}')"
    sql_update = f"UPDATE buku SET stock = stock - 1 WHERE id_buku = {id_buku_pinjam}"
    mycursor.execute(sql)
    mycursor.execute(sql_update)
    mydb.commit()
    
    
    print("Query successful")
    print("-------------------------")
    print(f"Book loaned to: {nama_user_pinjam}")

def show_buku():
   
    no = 0
    
  
    mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
    mycursor = mydb.cursor()
    
    
    mycursor.execute('SELECT * FROM buku;')
    cursor = mycursor.fetchall()
    
    
    print(mycursor.column_names)
    
    
    for data in cursor:
        no += 1
        print(data)
    

def show_user():
    
    no = 0
    
 
    mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
    mycursor = mydb.cursor()
    
 
    mycursor.execute('SELECT * FROM user;')
    cursor = mycursor.fetchall()
    
   
    print(mycursor.column_names)
    
    
    for data in cursor:
        no += 1
        print(data)    

def show_trans():
   
    no = 0
    
    
    mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
    mycursor = mydb.cursor()
    
 
    mycursor.execute('SELECT * FROM peminjaman;')
    result = mycursor.fetchall()
    
 
    print(mycursor.column_names)
    
    
    if mycursor.rowcount == 0: 
        print("Belum terdapat peminjaman")
    else:
        for data in result: 
            no += 1
            print(data)  


def cari_buku(): 
   
    seach_book = input("Masukkan Nama Buku: ")
    
   
    mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
    mycursor = mydb.cursor()
    
   
    mycursor.execute(f"SELECT * FROM buku WHERE nama_buku LIKE '%{seach_book}%';")
    cursor = mycursor.fetchall()
    
    
    if mycursor.rowcount == 0: 
        print("Buku tidak tersedia")
    else:
        columns = mycursor.description
        result = []
        for value in cursor: 
            tmp = {}
            for (index,column) in enumerate(value):
                tmp[columns[index][0]] = column
            result.append(tmp)
        print(pd.DataFrame(result))    


def kembalikan_buku():
   
    mydb = mysql.connector.connect(host=nama_host, user=user, passwd=password, database=db)
    mycursor = mydb.cursor()
    
    
    id_user_pinjam = input("Input ID Peminjaman: ")
    id_buku_pinjam = input("Input ID Buku: ")
    
   
    sql = f"DELETE FROM peminjaman WHERE id_user = {id_user_pinjam} AND id_buku = {id_buku_pinjam}"
    
   
    sql_update = f"UPDATE buku SET stock = stock + 1 WHERE id_buku = {id_buku_pinjam}"
    
  
    mycursor.execute(sql)
    mycursor.execute(sql_update)
    mydb.commit()
    
    
    print("Query berhasil dieksekusi")
    print("-------------------------")
    if mycursor.rowcount == 0:
        print("Tidak ada peminjaman buku tersebut") 
    else:
        print(f"Buku telah dikembalikan")


finished = False
while not finished:
    
   
    interface = """
    ....................LIBRARY MANAGEMENT.................... 
          1. Pendaftaran User Baru
          2. Pendaftaran Buku Baru
          3. Peminjaman Buku
          4. Tampilkan Daftar Buku
          5. Tampilkan Daftar User
          6. Tampilkan Daftar Peminjaman
          7. Cari Buku
          8. Pengembalian
          9. Exit
    """
    print(interface)
    
   
    choice = int(input('Masukkan nomor tugas:'))
    
    if choice == 1:
       
        print("-------------------------------------")
        add_new_user()
            
    elif choice == 2: 
        
        print("-------------------------------------")
        add_new_book()
        
    elif choice == 3: 
       
        print("-------------------------------------")
        add_new_trans()       
        
    elif choice == 4: 
        
        print("-------------------------------------")
        show_buku()         
        
    elif choice == 5: 
        
        print("-------------------------------------")
        show_user()         
        
    elif choice == 6:
       
        print("-------------------------------------")
        show_trans()        
        
    elif choice == 7: # Cari Buku
        #Tampilkan data
        print("-------------------------------------")
        cari_buku()                 
        
    elif choice == 8: 
       
        print("-------------------------------------")
        kembalikan_buku()            
        
        
    elif choice == 9: 
        is_finished = input('Apakah anda ingin keluar? (Y/N) ').upper()
        
        if is_finished == 'Y':
            finished == True
            break 
        else:
            pass
            
    else:
        print("Masukan angka sesuai dengan menu!") 