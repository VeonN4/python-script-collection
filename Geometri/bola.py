PHI = 3.14

r = float(input("Masukan jari-jari: "))

lb = lambda r: 4 * PHI * r**2
v = lambda r: 4/3 * PHI * r**3

print("Hasil Luas bola adalah:", lb(r), "cm2")
print("Hasil Volume adalah:", v(r), "cm3")
