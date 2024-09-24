x = int(input("Masukan nilai X:"))
y = int(input("Masukan nilai Y:"))
p = [x, y]

if x > 0 and y > 0:
    print("Titik P teletak di Kuadran 1")
elif x < 0 and y > 0:
    print("Titik P teletak di Kuadran 2")
elif x < 0 and y < 0:
    print("Titik P teletak di Kuadran 3")
elif x > 0 and y < 0:
    print("Titik P teletak di Kuadran 4")
else:
    print("Titik P terdapat di titik 0")