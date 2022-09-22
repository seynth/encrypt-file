# import yang penting aja
import os
import pyAesCrypt as aes

# fungsi recursive
# kalau fungsi ini dijalankan maka akan mengidentifikasi file atau folder di bawahnya 
def recursive(target):

    # standar looping
    for info in os.scandir(target):

        # kalau file
        if info.is_file():
            #encrypt


            #
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
