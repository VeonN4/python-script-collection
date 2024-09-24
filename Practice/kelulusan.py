nilai = int(input("Masukan nilai: "))

if nilai >= 75 and not nilai > 100:
    print("Lulus")
elif nilai > 100:
    print("Nilai tidak boleh lebih dari 100")
else:
    print("kamu gagal! Sakola dei")