print("="*30)
print('\tHITUNG VOLUME BALOK')
print("="*30)

panjang = int(input("Masukan nilai panjang\t: "))
nilaiSamaCheck = input("Samakan nilai lebar dan tinggi (y/n): ")

if nilaiSamaCheck == 'y':
    lebar = panjang
    tinggi = panjang
else:
    lebar = int(input("Masukan nilai lebar\t: ")) 
    tinggi = int(input("Masukan nilai tinggi\t: "))
volume = panjang * lebar * tinggi

print("Volume Balok\t\t:", volume, "cm3")