# nama = ["celio","shandy","farel","Ghazali","vito","afrizal","vito","adri",'yuyun',"rizal","adi","ifnu"]
# nama = ["celio",
#         "shandy",
#         "farel",
#         "Ghazali",
#         "vito",
#         "afrizal",
#         "vito",
#         "adri",
#         'yuyun',
#         "rizal",
#         "adi",
#         "ifnu"
# ]

# data = ["APD","APL","BASDAT","STRUKDAT","WEB","JARKOM"]
# print("sebelum: ")
# # print(nama)
# print("")
# print("Sesudah :")
# nama.append("afrizal")
# print(nama)

# print("sebelum: ")
# print(nama)
# print("")
# print("Sesudah :")
# nama.insert(2 , "afrizal")
# print(nama)
# nama[4]= "fufufafa"

# del nama[0]

# hapus = nama.pop(2)
# print (nama)
# print (hapus)

# print (nama[1:9:2])
# 
# data = matkul+nama

# matkul*3

# data = ["farel","celio",[1,2,["hai",23,2.3,True]]]

# print(data[2][2][0])
# print(data[::-1])
# print(data[2][2][::-1])

# # matkul = [1,2,3,4,[5,6,7]]
# matkul = [1,2,3,4,[5,6,7,[8,9,10]]]
# print(matkul[4][3][::-1])

# matkul = [1,2,3,4,5,6,7,8,9]
# matkul = [[1,2,3],[4,5,6]]
# matkul = [[1,2,3],[4,5,6],[8,9,10]]

# for i in matkul:
#     print(i, end="")
# for i in matkul:
#     # print(i)
#     for j in i:
#         print(i)

# nama = ("farrel", "vitp", "sahndy", "rijal")

# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
# absen, prodi, nim, nama = mahasiswa
# print (nama)

print(
"""

=========================
|   DATA MAHASISWA A24  |
=========================

|   1. TAMBAH DATA      |
|   1. TAMPILKAN DATA   |
|   1. UBAH DATA        |
|   1. HAPUS DATA       |
|   1. KELUAR           |
=========================

"""
)

data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")