x = 1
while x <= 12:
    print(x, end="\t")
    x += 1

y = 1
while y <= 12:
    print("")
    print(y, end='\t')
    z = 1
    while z <= 12:
        print(y*z, end='\t')
        z += 1
    y += 1
print()