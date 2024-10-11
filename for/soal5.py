jumlah = 0
count = 6

for i in range(1, count):
    print(i, end=" ")
    if i != count - 1:
        print("+", end=" ")
    jumlah = jumlah + i

print("=", jumlah)