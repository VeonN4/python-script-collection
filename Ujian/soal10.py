print("SOAL 11\n")

totalhargaBarang = int(input("Masukan total harga barang: Rp. "))

if totalhargaBarang >= 100000:
    hasil = (5/100) * totalhargaBarang
    print("Hasil Diskon Rp.", hasil)
    print("Total Barang Yang dibayar Rp.", totalhargaBarang - hasil)