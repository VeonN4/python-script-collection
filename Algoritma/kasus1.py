print("\tKasus 1")

# Menginput jam masuk dan jam pulang
jamMasuk = int(input("Masukan jam masuk (1-12): "))
jamPulang = int(input("Masukan jam pulang (1-12): "))

# Mengecek apakah jam masuk kurang dari 1 atau lebih dari 12
if jamMasuk > 12:
    print("Kamu tidak boleh memasukan angka lebih dari 12")
    exit()
elif jamMasuk < 1:
    print("Kamu tidak boleh memasukan angka kurang dari 1!")
    exit()

# Mengecek apakah jam pualngk kurang dari 1 atau lebih dari 12
if jamPulang > 12:
    print("Kamu tidak boleh memasukan angka lebih dari 12")
    exit()
elif jamPulang < 1:
    print("Kamu tidak boleh memasukan angka kurang dari 1!")
    exit()

# Mengecek jam masuk dan pulang, jika jam masuk lebih besar dari jam pulang maka, jam pulang ditambah 12 dikurangi jam masuk
if jamMasuk > jamPulang: # jammasuk = 10 jampulang 2
    jamKerja = (jamPulang + 12) - jamMasuk # Buat nyimpen data ini

# Mengecek jam masuk dan pulang, jika jam masuk kurang dari sama dengan jam pualng maka, jam pulang akan dikurangi jam masuk
elif jamMasuk <= jamPulang:
    jamKerja = jamPulang - jamMasuk # Sama aja buat nyimpen kalkulasi datanya

print("Lama kerja:", jamKerja, "jam")