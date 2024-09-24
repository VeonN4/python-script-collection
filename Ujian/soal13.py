inputHuruf = input("Masukan huruf: ")

vokal = ['a', 'i', 'u', 'e', 'o']
konsonan = ['b', 'd', 'c', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

if inputHuruf.lower().strip() in vokal:
    print("Huruf termasuk vokal")
else:
    print("Huruf termasuk konsonan")

# bukankeduanya = True

# for i in vokal:
    # if inputHuruf.lower().strip() == i:
        # print(inputHuruf, "adalah vokal")
        # bukankeduanya = False

# for i in konsonan:
    # if inputHuruf.lower().strip() == i:
        # print(inputHuruf, "adalah konsonan")
        # bukankeduanya = False

# if bukankeduanya:       
    # print(inputHuruf, "bukan keduanya")
