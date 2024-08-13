print("="*30)
print('\tHITUNG LUAS TRAPESIUM')
print("="*30)

tinggi = int(input("Masukan nilai tinggi\t: "))
sisiA = int(input("Masukan nilai sisi A\t: "))

nilaisamaCheck = input("Samakan nilai sisi? (y/n)\t: ")
nilaisamaCheck.lower().strip()

if nilaisamaCheck == "y":
    sisiB = sisiA
    sisiC = sisiA
    sisiD = sisiA
else:
    sisiB = int(input("Masukan nilai sisi B\t: "))
    sisiC = int(input("Masukan nilai sisi C\t: "))
    sisiD = int(input("Masukan nilai sisi D\t: "))

hasil = 0.5 * (sisiA + sisiB) * tinggi 
hasil2 = sisiA + sisiB + sisiC + sisiD

print("Luas Trapesium\t\t:", hasil, "cm2")
print("Keliling Trapesium\t\t:", hasil2, "cm2")