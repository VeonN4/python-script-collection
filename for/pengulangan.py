jumlah = 0

for i in range(5):
    for x in range(1):
        print(i+1, sep="+", end="")
    jumlah = jumlah + (i + 1)

print(f" = {jumlah}")

# """
# 0 = jumlah = 0 + 1
# 1 = jumlah = 1 + 2
# 2 = jumlah = 3 + 3
# 3 = jumlah = 6 + 4
# 4 = jumlah = 10 + 5
# """

# for i in range(3):
#     print(f"KELAS {10+i} PPLG {i+1}")