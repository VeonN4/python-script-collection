print("="*30)
print('\tHITUNG LUAS LINGKARAN')
print("="*30)

jari_jari = int(input("Masukan nilai jari-jari\t: "))
ruas_jari_jari = int(input("Masukan nilai ruas jari-jari\t: "))

hasil = int(22/7 * jari_jari**2)
hasil2 = int(2 * 22/7 * ruas_jari_jari)

print("Luas Lingkaran\t\t:", hasil, "cm2")
print("Keliling Lingkaran\t\t:", hasil2, "cm2")