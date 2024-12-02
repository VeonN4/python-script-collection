PHI = 3.14

r = int(input("Masukan jari-jari: "))
t = int(input("Masukan tinggi: "))

def tabung(phi, r, t):
    return phi * r**2 * t

print("Volume:", tabung(PHI, r, t), "cm3")