statusLampu = bool(input("Masukan status lampu: "))
warnaLampu = input("Masukan warna lampu: ").lower()

if statusLampu:
    if warnaLampu == "merah":
        print("Berhenti")
    elif warnaLampu == "kuning":
        print("Siap-siap")
    elif warnaLampu == "hijau":
        print("Jalan")
    else:
        print("Warna lampu salah rek")
else:
    print("JALAN")