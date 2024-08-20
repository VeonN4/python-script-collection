import math

print("="*30)
print("PROGRAM LINGKARAN")
print("="*30)

jari_jari = int(input("Masukan jari-jari: "))

hasilLuas = math.phi * jari_jari * jari_jari
hasilKeliling = math.phi * 2 * jari_jari

print("Luas:", hasilLuas, "cm2")
print("Keliling:", hasilKeliling, "cm")

