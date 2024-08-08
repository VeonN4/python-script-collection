print("="*30)
print('\tHITUNG LUAS LAYANG-LAYANG')
print("="*30)

diagonal1 = int(input("Masukan nilai diagonal A\t: "))
diagonal2 = int(input("Masukan nilai diagonal B\t: "))
sisiA = int(input("Masukan nilai sisi A\t: "))
sisiB = int(input("Masukan nilai sisi B\t: "))

hasil = 0.5 * diagonal1 * diagonal2
hasil2 = 2 * (sisiA + sisiB)

print("Luas Layang-layang\t\t:", hasil, "cm2")
print("Keliling Layang-layang\t\t:", hasil2, "cm2")