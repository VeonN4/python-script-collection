angka1 = int(input("Masukan angka ke 1: "))
angka2 = int(input("Masukan angka ke 2: "))

if angka2 * 2 >= angka1:
    angka1 *= 3
else:
    angka1 += angka2

print(angka1)