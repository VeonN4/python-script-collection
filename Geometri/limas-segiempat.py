lsisi1 = float(input("Masukan sisi ke-1: "))

confirm = input("Apakah kamu ingin menyamakan semua sisi? (y/n)")

if confirm.lower().strip() == "y" or confirm.lower().strip() == "yes":
    lsisi2 = lsisi3 = lsisi4 = lsisi5 = lsisi1
else:
    for i in range(2,4):
        lsisi2 = float(input("Masukan sisi ke-2: "))
        lsisi3 = float(input("Masukan sisi ke-3: "))
        lsisi4 = float(input("Masukan sisi ke-4: "))
        lsisi5 = float(input("Masukan sisi ke-5: "))

lalas = float(input("Masukan luas alas: "))
t = float(input("Masukan tinggi: "))

l = lambda a, b, c, d, e: a + b + c + d + e
v = lambda la, t: 1/3 * la * t

print("Hasil Luas adalah:", l(lsisi1, lsisi2, lsisi3, lsisi4, lsisi5), "cm2")
print("Hasil Volume adalah:", v(lalas, t), "cm3")

