x = int(input("Masukan Nilai X: "))
y = int(input("Masukan Nilai Y: "))
z = int(input("Masukan Nilai Z: "))

if x > y and x > z:
    print("Angka terbesar adalah:", x)
    if y < z:
        print("Angka ditengah adalah:", z)
        print("Angka terkecil adalah:", y)
    elif z < y:
        print("Angka ditengah adalah:", y)
        print("Angka terkecil adalah:", z)
elif y > x and y > z:
    print("Angka terbesar adalah:", y)
    if x < z:
        print("Angka ditengah adalah:", z)
        print("Angka terkecil adalah:", x)
    elif z < x:
        print("Angka ditengah adalah:", x)
        print("Angka terkecil adalah:", z)
else:
    print("Angka terbesar adalah:", z)
    if x < y:
        print("Angka ditengah adalah:", y)
        print("Angka terkecil adalah:", x)
    elif y < x:
        print("Angka ditengah adalah:", x)
        print("Angka terkecil adalah:", y)