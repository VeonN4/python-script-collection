print("\nMenghitung hari dengan sigma\n")

inputYear = int(input("Masukan tahun: "))
inputBulan = input("Masukan bulan: ")

if any(char.isdigit() for char in inputBulan):
    bulan = int(inputBulan)
else:
    bulan = inputBulan

months = {
    "januari": 31,
    "febuari": 28,
    "maret": 31,
    "april": 30,
    "mei": 31,
    "juni": 30,
    "juli": 31,
    "agustus": 30,
    "september": 31,
    "oktober": 30,
    "november": 31,
    "desember": 30
}

# Fungsi untuk mengecek tahun kabisat atau tidak
def cekTahun(year):
    if year % 400 == 0 or year % 4 == 0:
        print(f"\n{year} adalah tahun kabisat")
        months["febuari"] += 1
    elif year % 100 == 0 or year % 100 != 0 or year % 400 != 0 or year % 4 != 0:
        print(f"\n{year} Bukanlah tahun kabisat")

    return year # This is the most dumbest thing i ever do. Thank you!

# Fungsi untuk mengecek bulan dan mengeluarkan ada berapa hari dalam bulan tersebut, dengan input bulan dalam huruf ataupun angka.
def cekBulan(month):
    if isinstance(month, int):
        monthKey = list(months.keys())[int(month)-1]
        monthValue = list(months.values())[int(month)-1]
    elif isinstance(month, str):
        monthKey = list(months.keys()).index(month.lower())
        monthValue = list(months.values())[monthKey]
        
        monthKey = list(months.keys())[monthKey] # I got no idea what i'm doing in this 4 lines of codes, but it works though. I won't touch it again.

    return monthKey, monthValue

year = cekTahun(inputYear)
monthKey, monthValue = cekBulan(bulan)

print("Tahun", year, "Bulan", monthKey, "memiliki", monthValue, "hari\n")