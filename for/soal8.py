jumlah = 0
count = 10

for i in range(2, count + 1, 2):
    print(i, end=" ")
    if i != count - 1:
        print("+", end=" ")
    jumlah = jumlah + i

print("=", jumlah)