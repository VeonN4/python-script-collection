kalimat = input("Masukan kalimat: ")

ais = kalimat.split()

if not kalimat.startswith("Apakah"):
    ais.insert(0, "Apakah")
if not kalimat.endswith("?"):
    ais.append("?")

for i in range(len(ais)):
    print(ais[i], end=" ")