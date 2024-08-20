namaSiswa = input("Masukan Nama Siswa: ")
rentangNilai = int(input("Masukan Nilai (0-100): "))

if rentangNilai >= 90:
    print(f"Nilai {namaSiswa} adalah A")
elif rentangNilai >= 80:
    print(f"Nilai {namaSiswa} adalah B")
elif rentangNilai >= 70:
    print(f"Nilai {namaSiswa} adalah C")
else:
    print(f"Nilai {namaSiswa} adalah E")

