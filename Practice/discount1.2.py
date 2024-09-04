print("Toko Sigma")

barang1 = int(input("Masukan harga barang ke 1: "))
barang2 = int(input("Masukan harga barang ke 2: "))
barang3 = int(input("Masukan harga barang ke 3: "))
barang4 = int(input("Masukan harga barang ke 4: "))

totalHarga = barang1 + barang2 + barang3 + barang4

if totalHarga >= 200000:
    diskonHarga = (7.5/100) * totalHarga
    totalbayar = totalHarga - diskonHarga

    print("Total Harga:", totalHarga)
    print("Diskon:", diskonHarga)
    print("Total Bayar:", totalbayar)
else:
    print("Total Harga:", totalHarga)
    print("Total Bayar:", totalHarga)
