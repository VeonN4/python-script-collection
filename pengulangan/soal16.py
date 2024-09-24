panjang = 10

for x in range(panjang):
    print(" " * (panjang - x) + "*" * (2 * x -1))

for x in range(panjang, 0, -1):
    print(" " * (panjang - x) + "*" * (2 * x -1))