import random
import datetime

buah = ["apel", "mangga", "pisang"] 
print("Program Daftar Buah")

sekarang = datetime.datetime.now()
print("Waktu:", sekarang)

pilihan = input("Tambahkan buah baru? (ya/tidak): ")
if pilihan == "ya":
    buah_baru = input("Masukkan nama buah: ")
    buah.append(buah_baru)
print("Daftar buah:")
for b in buah:   
    print("-", b)

acak = random.choice(buah)
print("Buah yang dipilih secara acak:", acak)