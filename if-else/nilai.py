GRADE = ["A", "B", "C", "D", "E"]
nilaiSiswa = 0

inputNilai = int(input("Masukan nilai siswa: "))

if inputNilai >= 80:
    nilaiSiswa = GRADE[0]
elif inputNilai >= 80:
    nilaiSiswa = GRADE[1]
elif inputNilai >= 70:
    nilaiSiswa = GRADE[2]
elif inputNilai >= 55:
    nilaiSiswa = GRADE[3]
else:
    nilaiSiswa = GRADE[4]

print("Nilai siswa:", nilaiSiswa)