lsisi1 = float(input("Masukan sisi ke-1: "))

confirm = input("Apakah kamu ingin menyamakan semua sisi? (y/n)")

if confirm.lower().strip() == "y" or confirm.lower().strip() == "yes":
    lsisi2 = lsisi3 = lsisi1
else:
    for i in range(2,4):
        lsisi2 = float(input("Masukan sisi ke-2: "))
        lsisi3 = float(input("Masukan sisi ke-3: "))

t = float(input("Masukan tinggi (t): "))
tt = float(input("Masukan tinggi (T): "))
a = float(input("Masukan alas: "))

ls = lambda a, b, c, tt: (a + b + c) * tt
lp = lambda a, b, c, al, tt, t: (a + b + c) * tt + al * t
v = lambda a, t, tt: 1/2 * a * t * tt

print("Hasil Luas selimut:", ls(lsisi1, lsisi2, lsisi3, tt), "cm2")
print("Hasil Luas permukaan:", lp(lsisi1, lsisi2, lsisi3, a, tt, t), "cm2")
print("Hasil Volume:", v(a, t, tt), "cm3")