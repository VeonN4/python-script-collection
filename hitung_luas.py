import time

def display_menu():
    menu = ['Hitung Luas Persegi', 'Hitung Luas Kubus', 'Hitung Volume Balok', 'Hitung Luas Lingkaran', 'Hitung Luas Trapesium', 'Exit']

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

def hitung_luas_lingkaran():
    print("="*30)
    print('\tHITUNG LUAS LINGKARAN')
    print("="*30)

    jari_jari = int(input("Masukan nilai jari-jari\t: "))

    ruas_jari_jari = int(input("Masukan nilai ruas jari-jari\t: "))

    hasil = 22/7 * jari_jari**2
    hasil2 = 2 * 22/7 * ruas_jari_jari

    print("Luas Lingkaran\t\t:", hasil, "cm2")
    print("Keliling Lingkaran\t\t:", hasil2, "cm2")
    time.sleep(1.2)             
    print('\n')

def hitung_luas_trapesium():
    print("="*30)
    print('\tHITUNG LUAS TRAPESIUM')
    print("="*30)

    tinggi = int(input("Masukan nilai tinggi\t: "))
    sisi = int(input("Masukan nilai sisi\t: "))
    sisi2 = int(input("Masukan nilai sisi ke 2\t: "))

    hasil = 0.5 * (sisi + sisi2) * tinggi 

    print("Volume Balok\t\t:", hasil, "cm2")
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
        elif choice == 4:
            hitung_luas_lingkaran()
        elif choice == 5:
            hitung_luas_trapesium()
        else:
            print("Goodbye!")
            time.sleep(1)
            exit()

if __name__ == "__main__":
    main()

