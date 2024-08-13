print("="*30)
print('\tHITUNG LUAS BELAH KETUPAT')
print("="*30)

diagonal1 = int(input("Masukan nilai diagonal A\t: "))
diagonal2 = int(input("Masukan nilai diagonal B\t: "))
sisi = int(input("Masukan nilai sisi\t: "))

hasil = 0.5 * diagonal1 * diagonal2
hasil2 = 4 * sisi

print("Luas Belah Ketupat\t\t:", hasil, "cm2")
print("Keliling Belah Ketupat\t\t:", hasil2, "cm2")