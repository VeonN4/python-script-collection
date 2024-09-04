print("Toko Sigma Male \n")

totalhargabarang = int(input("Masukan total harga barang: "))

if totalhargabarang >= 100000:
    diskon = (90/100) * totalhargabarang
    totalhargabarang = totalhargabarang - diskon
    print("Total diskon:", diskon)

print("Total harga barang:", totalhargabarang)