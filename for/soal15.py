perkalian = int(input("Masukan perkalian: "))

print('x', end="\t")
print('\t'.join(str(i) for i in range(1, perkalian+1)))

for r in range(1,perkalian+1):
    print(r, end='\t')
    print('\t'.join(str(r*c) for c in range(1, perkalian+1)))