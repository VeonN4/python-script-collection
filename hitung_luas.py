import time

def display_menu():
    menu = ['Hitung Luas Persegi', 'Hitung Luas Kubus', 'Hitung Volume Balok', 'Hitung Luas Lingkaran', 'Hitung Luas Trapesium', 'Hitung Luas Segitiga', 'Hitung Luas Jajar Genjang', 'Hitung Luas Belah Ketupat', 'Hitung Luas Layang-layang', 'Hitung Luas Persegi Panjang', 'Exit']

    print("\tMENU HITUNG LUAS")

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

    hasil = int(22/7 * jari_jari**2)
    hasil2 = int(2 * 22/7 * ruas_jari_jari)

    print("Luas Lingkaran\t\t:", hasil, "cm2")
    print("Keliling Lingkaran\t\t:", hasil2, "cm2")
    time.sleep(1.2)             
    print('\n')

def hitung_luas_trapesium():
    print("="*30)
    print('\tHITUNG LUAS TRAPESIUM')
    print("="*30)

    tinggi = int(input("Masukan nilai tinggi\t: "))
    sisiA = int(input("Masukan nilai sisi A\t: "))
    nilaisamaCheck = input("Samakan nilai sisi? (y/n)\t: ")
    nilaisamaCheck.lower().strip()
    if nilaisamaCheck == "y":
        sisiB = sisiA
        sisiC = sisiA
        sisiD = sisiA
    else:
        sisiB = int(input("Masukan nilai sisi B\t: "))
        sisiC = int(input("Masukan nilai sisi C\t: "))
        sisiD = int(input("Masukan nilai sisi D\t: "))


    hasil = 0.5 * (sisiA + sisiB) * tinggi 
    hasil2 = sisiA + sisiB + sisiC + sisiD

    print("Luas Trapesium\t\t:", hasil, "cm2")
    print("Keliling Trapesium\t\t:", hasil2, "cm2")
    time.sleep(1.2)
    print('\n')

def hitung_luas_segitiga():
    print("="*30)
    print('\tHITUNG LUAS SEGITIGA')
    print("="*30)

    alas = int(input("Masukan nilai alas\t: "))
    tinggi = int(input("Masukan nilai tinggi\t: "))
    sisi = int(input("Masukan nilai sisi\t: "))

    hasil = 0.5 * alas * tinggi
    hasil2 = 3 * sisi

    print("Luas Segitiga\t\t:", hasil, "cm2")
    print("Keliling Segitiga\t\t:", hasil2, "cm2")
    time.sleep(1.2)
    print('\n')

def hitung_luas_segitiga():
    print("="*30)
    print('\tHITUNG LUAS SEGITIGA')
    print("="*30)

    alas = int(input("Masukan nilai alas\t: "))
    tinggi = int(input("Masukan nilai tinggi\t: "))
    sisi = int(input("Masukan nilai sisi\t: "))

    hasil = 0.5 * alas * tinggi
    hasil2 = 3 * sisi

    print("Luas Segitiga\t\t:", hasil, "cm2")
    print("Keliling Segitiga\t\t:", hasil2, "cm2")
    time.sleep(1.2)
    print('\n')

def hitung_luas_jajar_genjang():
    print("="*30)
    print('\tHITUNG LUAS JAJAR GENJANG')
    print("="*30)

    alas = int(input("Masukan nilai alas\t: "))
    tinggi = int(input("Masukan nilai tinggi\t: "))
    sisiA = int(input("Masukan nilai sisi A\t: "))
    sisiB = int(input("Masukan nilai sisi B\t: "))
  
    hasil = alas * tinggi
    hasil2 = 2 * (sisiA + sisiB)

    print("Luas Jajar Genjang\t\t:", hasil, "cm2")
    print("Keliling Jajar Genjang\t\t:", hasil2, "cm2")
    time.sleep(1.2)
    print('\n')

def hitung_luas_belah_ketupat():
    print("="*30)
    print('\tHITUNG LUAS BELAH KETUPAT')
    print("="*30)

    diagonal1 = int(input("Masukan nilai diagonal A\t: "))
    diagonal2 = int(input("Masukan nilai diagonal B\t: "))
    sisi = int(input("Masukan nilai sisi\t: "))

    hasil = 0.5 * diagonal1 * diagonal2
    hasil2 = 4 * sisi

    print("Luas Belah Ketupat\t\t:", hasil, "cm2")
    print("Keliling Belah Ketupat\t\t:", hasil2, "cm2")
    time.sleep(1.2)
    print('\n')

def hitung_luas_layang_layang():
    print("="*30)
    print('\tHITUNG LUAS LAYANG-LAYANG')
    print("="*30)

    diagonal1 = int(input("Masukan nilai diagonal A\t: "))
    diagonal2 = int(input("Masukan nilai diagonal B\t: "))
    sisiA = int(input("Masukan nilai sisi A\t: "))
    sisiB = int(input("Masukan nilai sisi B\t: "))

    hasil = 0.5 * diagonal1 * diagonal2
    hasil2 = 2 * (sisiA + sisiB)

    print("Luas Layang-layang\t\t:", hasil, "cm2")
    print("Keliling Layang-layang\t\t:", hasil2, "cm2")
    time.sleep(1.2)
    print('\n')

def hitung_luas_persegi_panjang():
    print("="*30)
    print('\tHITUNG LUAS PERSEGI PANJANG')
    print("="*30)

    panjang = int(input("Masukan nilai panjang\t: "))
    lebar = int(input("Masukan nilai lebar\t: "))

    hasil = panjang * lebar
    hasil2 = 2 * (panjang + lebar)

    print("Luas Layang-layang\t\t:", hasil, "cm2")
    print("Keliling Layang-layang\t\t:", hasil2, "cm2")
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
        elif choice == 6:
            hitung_luas_segitiga()
        elif choice == 7:
            hitung_luas_jajar_genjang()
        elif choice == 8:
            hitung_luas_belah_ketupat()
        elif choice == 9:
            hitung_luas_layang_layang()
        elif choice == 10:
            hitung_luas_persegi_panjang()
        else:
            print("Goodbye!")
            time.sleep(1)
            exit()

if __name__ == "__main__":
    main()

