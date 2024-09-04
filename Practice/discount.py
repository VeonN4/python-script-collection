print("="*40)
print("\tTOKO BUKU")
print("="*40, "\n")

totalhargaBarang = int(input("Masukan total harga barang: Rp. "))

hasil = (12.5/100) * totalhargaBarang

print("Hasil Diskon Rp.", hasil)
print("Total Barang Yang dibayar Rp.", totalhargaBarang - hasil)