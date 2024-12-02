angka = int(input("Masukan angka: "))

if angka < 10:
    print("Angka adalah satuan")
elif angka < 99:
    print("Angka adalah puluhan")
elif angka < 999:
    print("Angka adalah ratusan")    
elif angka < 999999:
    print("Angka adalah ribuan")    
elif angka < 9999999:
    print("Angka adalah jutaan")    