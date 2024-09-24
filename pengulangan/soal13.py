panjang = 10

"""
metode ke 1
"""

# for x in range(panjang):
#     for y in range(x+1):
#         print("*", end=" ")
#     print()

# for x in range(panjang - 1, 0, -1):
#     for y in range(0, x):
#         print("*", end=" ")
#     print()

for x in range(panjang):
    print("*" * x)
for x in range(panjang, 0 , -1):
    print("*" * x)