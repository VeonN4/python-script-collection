import time

def display_menu():
    menu = ['Hitung Luas Persegi', 'Hitung Luas Kubus', 'Hitung Volume Balok', 'Exit']

    print("MENU")

    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

    choice = int(input("Pilih Menu: "))

    return choice

def hitung_luas_persegi():
    print("="*30)
    print('\tHITUNG LUAS PERSEGI')
    print("="*30)

    sisi = int(input("Masukan nilai sisi\t: "))

    luas = sisi * sisi
    keliling = 4 * sisi

    print('Luas persegi\t\t:', luas, "cm2")
    print('Keliling persegi\t:', keliling, "cm2")
    time.sleep(1.2)
    print('\n')

def hitung_luas_kubus():
    print("="*30)
    print('\tHITUNG LUAS KUBUS')
    print("="*30)

    angka = int(input("Masukan nilai sisi\t: "))

    luas = 6 * angka

    print('Luas Kubus\t\t:', luas, "cm2")
    print('Volume Kubus\t\t:', angka, "cm2")
    time.sleep(1.2)
    print('\n')

def hitung_volume_balok():
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
    time.sleep(1.2)
    print('\n')

def main():
    while True:
        choice = display_menu()
        if choice == 1:
            hitung_luas_persegi()
        elif choice == 2:
            hitung_luas_kubus()
        elif choice == 3:
            hitung_volume_balok()
        else:
            print("Goodbye!")
            time.sleep(1)
            exit()

if __name__ == "__main__":
    main()

