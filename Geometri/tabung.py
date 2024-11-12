PHI = 3.14

r = float(input("Masukan jari-jari: "))
t = float(input("Masukan tinggi: "))

ls = lambda r, t: 2 * PHI * r * t
lp = lambda r, t: 2 * PHI * r * t + 2 * PHI * r**2
v = lambda r, t: PHI * r**2 * t

print("Hasil Luas Selimut adalah:", lp(r, t), "cm2")
print("Hasil Luas Permukaan adalah:", ls(r, t), "cm2")
print("Hasil Volume adalah:", v(r, t), "cm3")