# Encrypt-file
Bisa mengencrypt semua file yang ada di direktori yang sama dengan file ini (the real encrypt folder)

# Apa yang harus kamu siapkan?

 1. Buatlah folder namanya boleh bebas, contoh: ```folderTarget```
 
 2. Letakkan foto/gambar/video/folder terserah di dalam ```folderTarget```
 
 3. Kemudian copy file ```enc.py``` ke ```folderTarget```
 
 4. Kemudian bukalah ```cmd``` lalu rahkan ke folderTarget
 
 5. lalu ketikan perintah ```python .\enc.py``` bagi yang sudah menginstall python 3.x jika tidak ada python 
 
 6. Silahkan install python atau replace file ```enc.py``` dengan ```enc.exe``` yang sudah ada
 
 7. Kemudian klik 2 kali pada ```enc.exe``` dan tunggu
 
 8. Maka file kalian akan ter encrypt semua (hanya yang ada dalam ```folderTarget```) file yang ada di luar folderTarget tidak akan terencrypt :)
 
 
 Jika belum ada python: https://www.python.org/
 Selamat mencoba :)


# Keterangan

```python

# 
#
# coded by setyoBIASALAH
# jangan asal comot, ijin dlu ngapa
# 
#
import os                 # untuk berinteraksi pada OS kalian seperti create, read file
import pyAesCrypt as aes  # nah ini yang penting buat encrypt file kalian :)

# fungsi recursive
# kalau fungsi ini dijalankan maka akan mengidentifikasi file atau folder di bawahnya
# argumen target dibawah ini adalah folder yang akan kita encrypt
def recursive(target):

    # standar looping
    # jadi folder target akan kita baca lalu jika terdapat file maka kita akan encrypt
    # tapi jika ada folder lagi didalamnya maka akan mengulangi fungsi ini sampai ketemu file
    for info in os.scandir(target):

        # kalau file
        if info.is_file():
        
            # identifikasi path ke file target
            # misal file ini berada di folder
            # D:\folder1\folder2\folder3\target.txt
            path = info.path

            # mengambil folder saat ini misal:
            # D:\folder1\folder2\folder3\target.txt
            # nah kita ambil foldernya saja jadi D:\folder1\folder2\folder3\
            folder = os.path.dirname(path) #identifikasi folder dari path

            #nama file, misal:
            # target.txt
            file = info.name

            # membuat outfile yang akan kita encrypt nantinya
            # sebelum D:\folder1\folder2\folder3\target.txt
            # sesudah D:\folder1\folder2\folder3\enc-target.txt
            #
            encFile = os.path.join(folder, 'enc-'+file)

            # print(fnoext) #nama file tidak pakai extension
            # print(path) #nama file pakai extension

            #encrypt file :)
            # fungsi encrypt argumen pertamanya adalah infile/inputfile/file yang akan di encrypt
            # fungsi encrypt argumen keduanya adalah outfile/nama file setelah di encrypt
            # fungsi encrypt argumen ketiganya adalah password untuk mengencrypt file di argumen pertama
            # silahkan password boleh di custom
            encrypt(path, encFile, 'password123')
        else:
            # jika folder maka akan mengulangi fungsi ini sampai ketemu file
            recursive(info.path)


# encrypt file
# argumen pertama 'f' adalah file yang ingin kita encrypt/path ke file yang ingin kita encrypt
# contoh target.txt atau D:\folder1\folder2\folder3\target.txt 
#
# argumen kedua 'o' adalah output file setelah diencrypt 
# argumen ketiga 'p' adalah password
# (optional) argumen ke empat adalah buffersize defultnya 64kb
def encrypt(f, o, p):
    buffer = 128 * 1024
    aes.encryptFile(f, o, p, buffer)



current = os.getcwd()
# untuk mengambil "current working directory path"/path file saat ini
# kalau tidak percaya coba hilangkan tanda ## dibawah ini
## print('folder saat ini: ', current)

# menjalankan fungsi recursive()
recursive(current)

```
