jamKerjaNormal = 48
upahLembur = 3000

golongan = input("Masukan golongan (A-D): ")
jamKerja = int(input("Masukan jam kerja: "))
jamLembur = int(input("Masukan jam lembur: "))

if golongan.lower() == "a":
    upahPerJam = 4000
elif golongan.lower() == "b":
    upahPerJam = 5000
elif golongan.lower() == "c":
    upahPerJam = 6000
elif golongan.lower() == "d":
    upahPerJam = 7500

if jamKerja < jamKerjaNormal:
    upahTotal = upahPerJam * jamKerja
else:
    upahTotal = (upahPerJam * jamKerja) + (upahLembur * jamLembur)

print("Hasil upah:", upahTotal)



