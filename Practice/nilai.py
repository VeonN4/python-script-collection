nilaiKarakter = input("Nilai karakter: ").lower()
nilaiMTK = int(input("Nilai matematika: "))
nilaiINDO = int(input("Nilai indonesia: "))
nilaiENG = int(input("Nilai inggris: "))

if nilaiKarakter == "a" or nilaiKarakter == "b" and nilaiMTK >= 60 and nilaiINDO >= 70 and nilaiENG >= 55:
    print("\nKamu lulus")
else:
    print("\nKamu tidak lulus")