#Studi kasus 1

nilai = int(input("Masukkan nilai kamu:"))
if nilai >= 0 and nilai <= 100:
    if 80 <= nilai <= 89:
        print("Nilai kamu adalah A-")
    if 90 <= nilai <= 99:
        print("Nilai kamu adalah A-")
    

    if 60 <= nilai <= 69:
        print("Nilai kamu adalah B-")
    if 70 <= nilai <= 79:
        print("Nilai kamu adalah B+")
    

    if 40 <= nilai <= 49:
        print("Nilai kamu adalah C-")
    if 50 <= nilai <= 59:
        print("Nilai kamu adalah C+")
    
else :
    print("Nilainya kelebihan")

#studi kasus 2

gender =input("Pilih gender kamu (L/P) : ").upper()
if gender == "P":
    print("gender kamu adalah perempuan")
elif gender == "L" :
    print("Gender kamu adalah laki laki")  
else :
    print("masukkan antara L dan P saja")

