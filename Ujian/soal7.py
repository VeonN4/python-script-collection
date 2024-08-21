import math
print("="*30)
print("PROGRAM TABUNG")
print("="*30)

jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

luas_permukaan = (math.pi * jari**2) + (2 * math.pi * jari * tinggi)
volume = 2 * math.pi * jari * tinggi

memek = round(volume)

print("\nHasil Perhitungan:")
print(f"Volume Tabung: {volume}")
print(f"Luas Permukaan Tabung: {luas_permukaan}")
