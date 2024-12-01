import random

print("="*30)
print("\tCEK KHODAM")
print("="*30)

user = input("Masukan nama: ")

khodam1     =   ["Monyet", "Kucing", "Anjing", "Siluman", "Motor", "Knalpot", "Kodok", "Goblin"]
khodam2     =   ["Pemalas", "Julid", "Hideung", "Mio", "Sawah", "Vario", "Asli Sunda", "Dempes"]

resultKhodam1 = random.choice(khodam1)
resultKhodam2 = random.choice(khodam2)

print(f"Khodam {user} adalah {resultKhodam1} {resultKhodam2}")