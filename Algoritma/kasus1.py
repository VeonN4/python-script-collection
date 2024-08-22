print("\tKasus 1")

# Menginput jam masuk , jam pulang, dan menginisiasi variabel hour
jamMasuk = int(input("Masukan jam masuk (1-12): "))
jamPulang = int(input("Masukan jam pulang (1-12): "))
hour = 0


# Mengecek apakah jam masuk kurang dari 1 atau lebih dari 12
if jamMasuk > 12:
    print("Kamu tidak boleh memasukan angka lebih dari 12")
elif jamMasuk < 1:
    print("Kamu tidak boleh memasukan angka kurang dari 1!")

# Mengecek apakah jam pualngk kurang dari 1 atau lebih dari 12
if jamPulang > 12:
    print("Kamu tidak boleh memasukan angka lebih dari 12")
elif jamPulang < 1:
    print("Kamu tidak boleh memasukan angka kurang dari 1!")

# Mengecek apakah jam kurang dari 10. Jika iya, akan menambahkan 12 dan mengecek apakah jam sama dengan 12
if jamPulang < 10:
    jamPulang = 12 + jamPulang
if jamMasuk < 10:
    jamMasuk = 12 + jamMasuk

            

# Pengulangan untuk mencari lama kerja
if jamMasuk < jamPulang:
    for i in range(jamMasuk, jamPulang):
        hour += 1
elif jamPulang < jamMasuk:
    for i in range(jamPulang, jamMasuk):
        hour += 1

print("Lama kerja:", hour, "jam")