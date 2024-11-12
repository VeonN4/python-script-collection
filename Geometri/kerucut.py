PHI = 3.14

r = float(input("Masukan jari-jari: "))
t = float(input("Masukan tinggi: "))
s = float(input("Masukan sisi: "))

ls = lambda r, s: PHI * r * s
lp = lambda r, s: PHI * r * s + PHI * r**2
v = lambda r, t: 1/3 * PHI * r**2 * t

print("Hasil Luas Selimut adalah:", lp(r, s), "cm2")
print("Hasil Luas Permukaan adalah:", ls(r, s), "cm2")
print("Hasil Volume adalah:", v(r, t), "cm3")