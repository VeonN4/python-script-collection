print("="*30)
print('\tHITUNG LUAS JAJAR GENJANG')
print("="*30)

alas = int(input("Masukan nilai alas\t: "))
tinggi = int(input("Masukan nilai tinggi\t: "))
sisiA = int(input("Masukan nilai sisi A\t: "))
sisiB = int(input("Masukan nilai sisi B\t: "))

hasil = alas * tinggi
hasil2 = 2 * (sisiA + sisiB)

print("Luas Jajar Genjang\t\t:", hasil, "cm2")
print("Keliling Jajar Genjang\t\t:", hasil2, "cm2")