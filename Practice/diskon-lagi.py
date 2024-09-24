totalBelanja = int(input("Masukan total belanja: "))
diskon = 0
total = totalBelanja

if totalBelanja >= 1000000:
    diskon = 2 / 100 * totalBelanja
elif totalBelanja >= 500000:
    diskon = 4 / 100 * totalBelanja
elif totalBelanja >= 100000:
    diskon = 6 / 100  * totalBelanja

total = totalBelanja - diskon

print("Total diskon:", diskon)
print("Total harga:", total)