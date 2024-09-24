GRADE = ["A", "B", "C", "D", "E"]
nilaiSiswa = 0

inputNilai = int(input("Masukan nilai siswa: "))

if inputNilai >= 90 and not inputNilai > 100:
    nilaiSiswa = GRADE[0]   
elif inputNilai >= 80 and inputNilai <= 89:
    nilaiSiswa = GRADE[1]
elif inputNilai >= 70 and inputNilai <= 79:
    nilaiSiswa = GRADE[2]
elif inputNilai >= 55 and inputNilai <= 59:
    nilaiSiswa = GRADE[3]
elif inputNilai < 55:
    nilaiSiswa = GRADE[4]
else:   
    print("Nilai tidak boleh dari 100!")

print("Nilai siswa:", nilaiSiswa)
