print("Menghitung hari dengan sigma")

#inputYear = int(input("Masukan tahun: "))
#inputBulan = int(input("Masukan bulan: "))

month = {
    "Januari": 31,
    "Febuari": 28,
    "Maret": 31,
    "April": 30,
    "Mei": 31,
    "Juni": 30,
    "Juli": 31,
    "Agustus": 30,
    "September": 31,
    "Oktober": 30,
    "November": 31,
    "Desember": 30
}

def cekTahun(year):
    if year % 400 == 0 or year % 4 == 0:
        print(f"{2024} adalah tahun kabisat")
        month["Febuari"] += 1
    elif year % 100 == 0 or year % 100 != 0 or year % 400 != 0 or year % 4 != 0:
        print(f"{year} Bukanlah tahun kabisat")

idx for idx, key in :
    print(month)

#cekTahun(inputYear)
print("Bulan", month)